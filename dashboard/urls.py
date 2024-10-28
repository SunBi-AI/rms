from django.urls import path
from dashboard.views import *


app_name = "dashboard"

urlpatterns = [
    path('',DashboardView.as_view(), name='index'),
    path("filemanager/", FileManagerView.as_view(), name="filemanager"),
    path("basic-settings/", SettingsView.as_view(), name="settings"),
    path("informative-settings/", AboutSettingsView.as_view(), name="aboutus"),

    path("page/add", PageView.as_view(), name="addpage"),
    path("page/list", PageListView.as_view(), name="listpage"),
    path("page/edit", PageEditView.as_view(), name="editpage"),
    
    path("add", Items.as_view(), name="add"),
    path("list", ItemsListView.as_view(), name="list"),
    path("edit", ItemsEditView.as_view(), name="edit"),

    path("delete/", DeleteView.as_view(), name="delete"),
    path("delete/final/", DeleteFinalView.as_view(), name="deletefinal"),


]
