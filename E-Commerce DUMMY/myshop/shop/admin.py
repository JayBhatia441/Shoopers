from django.contrib import admin
from shop.models import Customer,Product,ShippingAddress,CartItem,Order,CategoryElectronics,CategoryBooks,CategoryClothes,CategoryFootwear

# Register your models here.
admin.site.register(Customer)

admin.site.register(Product)
admin.site.register(ShippingAddress)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(CategoryBooks)
admin.site.register(CategoryClothes)
admin.site.register(CategoryFootwear)
admin.site.register(CategoryElectronics)
