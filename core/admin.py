from django.contrib import admin

# Register your models here.
class Admin(admin.ModelAdmin):
    pass

admin.site.register(Core, Admin)
