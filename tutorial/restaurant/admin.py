from django.contrib import admin
from restaurant.models import Food, FoodCategory, Order

@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'decription')
    list_display = ('name', 'description', 'get_created_at')
    list_per_page = 10 
    readonly_fields = ('get_created_at',)
    ordering =('-created_at', )
    fieldsets  = [
        ('Details', {
            'fields': ('name', 'description' ),
        }),
    ]

    def get_created_at(self, obj:FoodCategory):
        return obj.created_at
    get_created_at.short_description= "DATE CREATED"

    # def has_delete_permission(self, request, obj=None):
    #     return False # False the Button Delete

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'price')
    list_per_page = 10
    search_fields = ('category__name', 'name', 'price') 
    readonly_fields = ('get_created_at',)
    ordering =('-created_at', )
    list_filter = ('category',)

    fieldsets  = [
        ('Food Details', {
            'fields': ('category','name', 'price' ),
        }),
    ]

    def get_created_at(self, obj:FoodCategory):
        return obj.created_at
    get_created_at.short_description= "DATE CREATED"

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'get_created_at', )
    list_per_page = 10
    search_fields = ('customer__first_name', 'customer__last_name') 
    readonly_fields = ('get_created_at','get_full_name',)
    ordering =('-created_at', )
    fieldsets  = [
        ('Food Details', {
            'fields': ('foods','customer',),
        }),
    ]

    def get_created_at(self, obj:Order):
        return obj.created_at
    get_created_at.short_description= "DATE CREATED"


    def get_full_name(self, obj:Order):
        return obj.customer.get_full_name()
    get_full_name.short_description= "NAME"