from django.contrib import admin
from .models import Collection,Product,Customer,Cart,Order

admin.site.register(Product)
admin.site.register(Collection)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)