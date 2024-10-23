from django.shortcuts import render,redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
# Create your views here.
from menu.models import *
from .models import *
from django.db.models import Prefetch, Count
from .forms import *

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/parts/index.html')
    
class FileManagerView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/parts/filemanager.html')

class SettingsView(View):
    def get(self, request, *args, **kwargs):
        settings = SiteSettings.objects.first()
        form = SiteSettingsForm(instance=settings)
        return render(request, 'dashboard/parts/setting.html', {'form': form})

    def post(self, request, *args, **kwargs):
        settings = SiteSettings.objects.first()
        form = SiteSettingsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            return redirect('dashboard:settings')  # Make sure 'settings_view' is the correct URL name
        return render(request, 'dashboard/parts/setting.html', {'form': form})

class AboutSettingsView(View):
    def get(self, request, *args, **kwargs):
        settings = AboutSettings.objects.first()
        about_form = AboutSettingsForm(instance=settings)

        return render(request, 'dashboard/parts/setting/info_setting.html', {
            'about_form': about_form,
        })

    def post(self, request, *args, **kwargs):
        settings = AboutSettings.objects.first()
        about_form = AboutSettingsForm(request.POST, instance=settings)

        if about_form.is_valid():
            # If there is no settings instance, create one
            about_form.save()

            return redirect('dashboard:settings')

        return render(request, 'dashboard/parts/setting/info_setting.html', {
            'about_form': about_form,
        })



class PageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/page/add.html')
    
class PageListView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'dashboard/page/list.html')
    

class PageEditView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/page/edit.html')
    
class DeleteHelper:
    def get_objects(self, ids, model, type_title, reverse_name=None, title_generator=None, kwargs_generator=None):
        objects = []
        objects_org = []
        try:
            for obj_id in ids:
                try:
                    obj = model.objects.get(id=obj_id)
                    title = title_generator(obj) if title_generator else obj.id
                    url = reverse(reverse_name, kwargs=kwargs_generator(obj)) if reverse_name else "#"

                    objects_org.append(obj)
                    objects.append({
                        "id": obj.id,
                        "type": type_title,
                        "title": title,
                        "url": url
                    })
                except model.DoesNotExist:
                    pass
        except Exception as e:
            print(e)
            pass
        return objects, objects_org

    def get_menu(self, ids):
        def menu_title(menu):
            return menu.items_name
        def menu_kwargs(menu):
            return {"id": menu.id}
        return self.get_objects(ids,MenuItem, "MenuItem", "menu:menuedit", menu_title, menu_kwargs)
    def get_category(self, ids):
        def category_title(category):
            return category.name
        def category_kwargs(category):
            return {"id": category.id}
        return self.get_objects(ids,Category, "Category", "menu:categoryedit", category_title, category_kwargs)
    def get_subcategory(self, ids):
        def subcategory_title(subcategory):
            return subcategory.name
        def subcategory_kwargs(subcategory):
            return {"id": subcategory.id}
        return self.get_objects(ids,Subcategory, "Subcategory", "menu:sub-categoryedit", subcategory_title, subcategory_kwargs)


    def get_titles(self, post_type: str, total):
        if post_type == "menu":
            return "Menus" if total > 1 else "Menu"
        elif post_type == "category":
            return "Categories" if total > 1 else "Caterory"
        elif post_type == "subcategory":
            return "Sub-Categories" if total > 1 else "Sub-Category"
        return "Objects"

    def get_delete_objects(self, delete_type, selected_ids=None):
        if selected_ids is None:
            selected_ids = []

        objects = []
        originals = []

        if selected_ids:
            if delete_type == "menu":
                objects, originals = self.get_menu(selected_ids)
            elif delete_type == "category":
                objects, originals = self.get_category(selected_ids)
            elif delete_type == "subcategory":
                objects, originals = self.get_subcategory(selected_ids)
        return objects, originals


class DeleteFinalView(View, DeleteHelper):
    def get(self, request, *args, **kwargs):
        return redirect("dashboard:index")

    def post(self, request, *args, **kwargs):
        delete_type = request.POST.get("_selected_type", None)
        selected_ids = request.POST.getlist("_selected_id", [])
        back = request.POST.get("_back_url", None)
        objects, originals = self.get_delete_objects(delete_type, selected_ids)

        for original in originals:
            try:
                object_title = original.id
                original.delete()
                messages.success(request, f"Successfully deleted #{object_title}")
            except Exception as e:
                messages.error(request, str(e))

        if back:
            return redirect(back)
        return redirect("dashboard:index")


@method_decorator(csrf_exempt, name='dispatch')
class DeleteView(View, DeleteHelper):
    def post(self, request, *args, **kwargs):
        selected_ids = request.POST.getlist("_selected_id", [])
        delete_type = request.POST.get("_selected_type", None)
        back = request.POST.get("_back_url", None)
        objects, originals = self.get_delete_objects(delete_type, selected_ids)

        # if not objects:
        #     raise Exception("No objects to delete")

        total_objects = len(objects)
        return render(request, 'dashboard/parts/delete.html', context={
            "objects": objects,
            "type_title": self.get_titles(delete_type, total_objects),
            "back": back,
            "type": delete_type,
            "total": total_objects
        })