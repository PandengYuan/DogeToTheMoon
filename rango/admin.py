from django.contrib import admin
from rango.models import Category, Product
from rango.models import UserProfile

# add category to admin page
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

# add product to admin page
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Product, ProductAdmin)


# add userprofile to admin page 
admin.site.register(UserProfile)