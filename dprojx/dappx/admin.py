from django.contrib import admin


# dappx/admin.py

from dappx.models import UserProfileInfo,productcategories,products,orders,cartItem,orders,Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment','product','user','status']
    list_filter = ['status']


admin.site.register(UserProfileInfo)
admin.site.register(products)
admin.site.register(productcategories)
admin.site.register(orders)
admin.site.register(cartItem)
admin.site.register(Comment,CommentAdmin)
# admin.site.register(userType)
