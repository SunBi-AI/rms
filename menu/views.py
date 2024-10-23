from django.shortcuts import render, redirect
from django.views import View
from .models import MenuItem, Category, Subcategory
from .forms import MenuForm, CategoryForm, SubcategoryForm
from django.contrib import messages
from django.http import JsonResponse
from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator,  PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse



class MenuList(View):
    def get(self, request):
        items = MenuItem.objects.all()
        return render(request, "dashboard/menu/list.html", context={"items": items})


class MenuView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        form = MenuForm()
        return render(request, "dashboard/menu/add.html", context={"form": form, "categories": categories})

    def post(self, request, *args, **kwargs):
        form = MenuForm(request.POST)

        categories = Category.objects.all()
        if form.is_valid():
            form.save()
            messages.success(request, "Menu item added successfully")
            return redirect("menu:menulist")
        else:
            messages.error(request, "Error in the form")
        return render(request, "dashboard/menu/add.html", context={"form": form, "categories": categories})

        
class MenuEdit(View):
    def get(self, request, *args, **kwargs):
        item_id = kwargs.get("id")
        item = get_object_or_404(MenuItem, id=item_id)
        categories = Category.objects.all()
        subcategories = Subcategory.objects.filter(category=item.items_category)

        return render(
            request,
            "dashboard/menu/edit.html",
            context={
                "itemid": item_id,
                "name": item.items_name,
                "description": item.items_description,
                "price": item.items_price,
                "image": item.items_image,
                "category": item.items_category,
                "subcategory": item.sub_category,
                "categories": categories,
                "subcategories": subcategories,
            },
        )

    def post(self, request, *args, **kwargs):
        item_id = kwargs.get("id")
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        image = request.FILES.get("image")
        category_id = request.POST.get("category")
        subcategory_id = request.POST.get("subcategory")
        available = request.POST.get("available") == "on"

        try:
            item = get_object_or_404(MenuItem, id=item_id)
            
            if not name:
                raise Exception("Menu item name is required")

            # Update fields
            item.items_name = name
            item.items_description = description
            item.items_price = price
            item.items_category_id = category_id
            item.sub_category_id = subcategory_id

            if image:  # Only update the image if a new one is uploaded
                item.items_image = image

            item.save()

            messages.success(request, "Menu item updated successfully")
            return redirect("menu:menulist")  # Make sure 'menulist' is the correct URL name
        except Exception as e:
            messages.error(request, str(e))

        categories = Category.objects.all()
        subcategories = Subcategory.objects.filter(category_id=category_id)

        return render(
            request,
            "dashboard/menu/edit.html",
            context={
                "itemid": item_id,
                "name": name,
                "description": description,
                "price": price,
                "image": image,
                "category": category_id,
                "subcategory": subcategory_id,
                "categories": categories,
                "subcategories": subcategories,
                "available": available,
            },
        )
class MenuAjax(View):
    def get(self, request, *args, **kwargs):
        draw = int(request.GET.get("draw", 1))
        start = int(request.GET.get("start", 0))
        length = int(request.GET.get("length", 10))
        search_value = request.GET.get("search[value]", None)
        page_number = (start // length) + 1

        menu_items = MenuItem.objects.all()
        if search_value:
            menu_items = menu_items.filter(
                Q(items_name__icontains=search_value) | Q(items_description__icontains=search_value),
                Q(items_name__icontains=search_value) | Q(items_description__icontains=search_value)
            )

        menu_items = menu_items.order_by("items_name")

        paginator = Paginator(menu_items, length)

        try:
            page_menu_items = paginator.page(page_number)
        except EmptyPage:
            page_menu_items = []

        data = []
        for item in page_menu_items:
            data.append(
                [
                    item.items_name,
                    item.items_price,
                    item.items_category.name if item.items_category else "N/A",  # Serialize category name
                    item.sub_category.name if item.sub_category else "N/A",  # Serialize sub-category name
                    self.get_action(item.id),
                ]
            )

        return JsonResponse(
            {
                "draw": draw,
                "recordsTotal": MenuItem.objects.count(),
                "recordsFiltered": menu_items.count(),
                "data": data,
            },
            status=200,
        )

    def get_action(self, post_id):
        edit_url = reverse('menu:menuedit', kwargs={'id': post_id})
        delete_url = reverse('dashboard:delete')
        backurl = reverse('menu:menulist')
        return f'''
            <form method="post" action="{delete_url}" class="button-group">
                <a href="{edit_url}" class="btn btn-success btn-sm">Edit</a>

                <input type="hidden" name="_selected_id" value="{post_id}" />
                <input type="hidden" name="_selected_type" value="menu" />
                <input type="hidden" name="_back_url" value="{backurl}" />
                <button type="submit" class="btn btn-danger btn-sm">Delete</button>
            </form>
        '''
class CategoryView(View):
    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category saved successfully")
            return redirect("menu:category")
        else:
            messages.error(request, "Please correct the errors below.")
            return render(
                request,
                "dashboard/category/add.html",
                {"form": form, "categories": Category.objects.all()},
            )

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        form = CategoryForm()
        return render(
            request,
            "dashboard/category/add.html",
            {"form": form, "categories": categories},
        )
class CategoryListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "dashboard/category/list.html", {"categories": Category.objects.all()})

class CategoryAjaxView(View):
    def get(self, request, *args, **kwargs):
        try:
            draw = int(request.GET.get("draw", 1))
            start = int(request.GET.get("start", 0))
            length = int(request.GET.get("length", 10))
            search_value = request.GET.get("search[value]", None)
            page_number = (start // length) + 1

            categories = Category.objects.all()
            if search_value:
                categories = categories.filter(
                    Q(name__icontains=search_value)
                )

            categories = categories.order_by("id")
            paginator = Paginator(categories, length)
            categories_page = paginator.page(page_number)

            data = []
            for category in categories_page:
                data.append(
                    [
                        category.id,
                        category.name,
                        self.get_action(category.id),
                    ]
                )

            return JsonResponse(
                {
                    "draw": draw,
                    "recordsTotal": paginator.count,
                    "recordsFiltered": paginator.count,
                    "data": data,
                },
                status=200,
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def get_action(self, category_id):
        edit_url = reverse('menu:categoryedit', kwargs={'id': category_id})
        delete_url = reverse('dashboard:delete')
        backurl = reverse('menu:category')
        return f'''
            <form method="post" action="{delete_url}" class="button-group">

                <input type="hidden" name="_selected_id" value="{category_id}" />
                <input type="hidden" name="_selected_type" value="category" />
                <input type="hidden" name="_back_url" value="{backurl}" />
                <button type="submit" class="btn btn-danger btn-sm">Delete</button>
            </form>
        '''

class SubCategoryView(View):
    def post(self, request):
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Subcategory saved successfully")
            return redirect("menu:sub-category")
        else:
            messages.error(request, "Please correct the errors below.")
            categories = Category.objects.all()
            return render(
                request,
                "dashboard/subcategory/add.html",
                {"form": form, "categories": categories},
            )

    def get(self, request, *args, **kwargs):
        form = SubcategoryForm()
        categories = Category.objects.all()
        return render(
            request,
            "dashboard/subcategory/add.html",
            {"form": form, "categories": categories},
        )


class SubcategoryListView(View):
    def get(self, request, category_id):
        # Fetch subcategories that belong to the selected category
        subcategories = Subcategory.objects.filter(category_id=category_id).values(
            "id", "name"
        )
        return JsonResponse(list(subcategories), safe=False)

class SubcategoryList(View):
    def get(self, request, *args, **kwargs):
        return render(request, "dashboard/subcategory/list.html")

class SubCategoryAjaxView(View):
    def get(self, request, *args, **kwargs):
        try:
            # Get the draw parameter sent by DataTables
            draw = int(request.GET.get("draw", 1))
            start = int(request.GET.get('start', 0))
            length = int(request.GET.get('length', 10))

            # Fetch subcategories and paginate
            subcategories = Subcategory.objects.all().order_by("id")
            paginator = Paginator(subcategories, length)

            try:
                subcategories_page = paginator.page((start // length) + 1)
            except PageNotAnInteger:
                subcategories_page = paginator.page(1)
            except EmptyPage:
                subcategories_page = paginator.page(paginator.num_pages)

            data = []
            for subcategory in subcategories_page:
                data.append(
                    [
                        subcategory.name,
                        self.get_action(subcategory.id),
                    ]
                )

            return JsonResponse({
                "draw": draw,
                "recordsTotal": paginator.count,
                "recordsFiltered": paginator.count,
                "data": data,
            }, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def get_action(self, subcategory_id):
        edit_url = reverse('menu:sub-categoryedit', kwargs={'id': subcategory_id})
        delete_url = reverse('dashboard:delete')
        backurl = reverse('menu:sub-category') 
        
        return f'''
            <form method="post" action="{delete_url}" class="button-group">
                <input type="hidden" name="_selected_id" value="{subcategory_id}" />
                <input type="hidden" name="_selected_type" value="subcategory" />
                <input type="hidden" name="_back_url" value="{backurl}" />
                <button type="submit" class="btn btn-danger btn-sm">Delete</button>
            </form>
        '''

