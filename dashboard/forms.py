from django import forms
from .models import SiteSettings,AboutSettings



class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = [
            'website_name',
            'location',
            'website_fav',
            'website_logo',
            'website_feature1',
            'website_feature2',
            'website_scrollimg1',
            'website_scrollimg2',
            'website_scrollimg3',
            'website_scrollimg4',
            'website_scrollimg5',
            'website_scrollimg6',
            'website_baner',
        ]


class AboutSettingsForm(forms.ModelForm):
    class Meta:
        model = AboutSettings
        fields = [
            'about_title',
            'about_description',
            'about_image',
            'owner_img',
            'owner_name',
            'manager_img',
            'manager_name',
            'fran_manager_img',
            'fran_manager_name',
            'cook_name',
            'cook_img',
        ]
