from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    items_name = models.CharField(max_length=100)
    items_image = models.TextField(blank=True, null=True)
    items_price = models.DecimalField(max_digits=10, decimal_places=2)
    items_description = models.TextField(blank=True, null=True)
    items_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.items_name
