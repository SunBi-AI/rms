from django.urls import path
from .views import *


app_name = "dashboard"

urlpatterns = [
    path("manager/", FilterManagerView.as_view(), name="manager"),
    path("page/add", FilterPageView.as_view(), name="addpage"),
    path("page/list", FilterPageListView.as_view(), name="listpage"),
    path("page/edit", FilterPageEditView.as_view(), name="editpage"),
    
    path("add", FilterItems.as_view(), name="add"),
    path("list", FilterItemsListView.as_view(), name="list"),
    path("edit", FilterItemsEditView.as_view(), name="edit"),

    path("delete/", FilterDeleteView.as_view(), name="delete"),
    path("delete/final/", FilterDeleteFinalView.as_view(), name="deletefinal"),


]
