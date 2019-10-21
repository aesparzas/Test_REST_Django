from django.contrib import admin
from house.models import House

# Register your models here.


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    pass