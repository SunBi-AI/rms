from django.urls import path
from dashboard.views import *


app_name = "dashboard"

urlpatterns = [
    path('admin/',DashboardView.as_view(), name='index'),
    path("filemanager/", FileManagerView.as_view(), name="filemanager"),
    path("basic-settings/", SettingsView.as_view(), name="settings"),
    path("informative-settings/", AboutSettingsView.as_view(), name="aboutus"),
    path("page/add", PageView.as_view(), name="addpage"),
    path("page/list", PageListView.as_view(), name="listpage"),
    path("page/edit", PageEditView.as_view(), name="editpage"),
    
    path("delete/", DeleteView.as_view(), name="delete"),
    path("delete/final/", DeleteFinalView.as_view(), name="deletefinal"),


]
