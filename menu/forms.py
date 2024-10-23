from django import forms
from .models import MenuItem, Category, Subcategory

class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = [
            "items_name",
            "items_image",
            "items_description",
            "items_price",
            "items_category",
            "sub_category",
        ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ["name", "category"]
