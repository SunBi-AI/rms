from django.urls import path
from .views import * 

app_name = "menu"

urlpatterns = [
    path("menu/add", MenuView.as_view(), name="menu"),
    path("menu/edit/<id>", MenuEdit.as_view(), name="menuedit"),
    path("menu/list", MenuList.as_view(), name="menulist"),
    path("menu/ajax", MenuAjax.as_view(), name="menuajax"),


    path("menu/<str:category>/", MenuView.as_view(), name="menu_by_category"),
    path("category/", CategoryView.as_view(), name="category"),
    path("category/list/", CategoryListView.as_view(), name="categorylist"),
    path("category/edit/<id>/", CategoryView.as_view(), name="categoryedit"),
    path('categoryajax',CategoryAjaxView.as_view(), name="categoryAjax"),
    path("sub-category/", SubCategoryView.as_view(), name="sub-category"),
    path("sub-category/edit/<id>/", SubCategoryView.as_view(), name="sub-categoryedit"),
    path('subcategories/<int:category_id>/', SubcategoryListView.as_view(), name='subcategory-list'),
    path('subcategories/list/', SubcategoryList.as_view(), name='subcategories-list'),
    path('subcategoryajax',SubCategoryAjaxView.as_view(), name="sub_categoryAjax"),
    
]
