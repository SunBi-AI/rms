from django.db import models


class SiteSettings(models.Model):
    website_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    website_fav = models.TextField(blank=True, null=True)
    website_logo = models.TextField(blank=True, null=True)
    website_feature1 = models.TextField(blank=True, null=True)
    website_feature2 = models.TextField(blank=True, null=True)
    website_scrollimg1 = models.TextField(blank=True, null=True)
    website_scrollimg2 = models.TextField(blank=True, null=True)
    website_scrollimg3 = models.TextField(blank=True, null=True)
    website_scrollimg4 = models.TextField(blank=True, null=True)
    website_scrollimg5 = models.TextField(blank=True, null=True)
    website_scrollimg6 = models.TextField(blank=True, null=True)
    website_baner = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.website_name

class AboutSettings(models.Model):
    about_title = models.CharField(max_length=255, blank=True, null=True)  # Optional field
    about_description = models.TextField(blank=True, null=True)  # Optional field
    about_image = models.TextField(blank=True, null=True)  # Optional fiel
    owner_img = models.TextField(blank=True, null=True)  # Optional field
    owner_name = models.CharField(max_length=100, blank=True, null=True)  # Optional field
    manager_img = models.TextField(blank=True, null=True)  # Optional field
    manager_name = models.CharField(max_length=100, blank=True, null=True)  # Optional field
    fran_manager_img = models.TextField(blank=True, null=True)  # Optional field
    fran_manager_name = models.CharField(max_length=100, blank=True, null=True)  # Optional field
    cook_name = models.CharField(max_length=100, blank=True, null=True)  # Optional field
    cook_img = models.TextField(blank=True, null=True)  # Optional field

    def __str__(self):
        return self.about_title or 'Untitled About Settings'

