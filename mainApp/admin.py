from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register((Maincategory,Subcategory,Brand,Product,Buyer,Wishlist,Checkout,CheckoutProduct,Newslatter,Contact))#Must be pass as Tuple

@admin.register(Maincategory)
class MaincategoryAdmin(admin.ModelAdmin):
    list_display=['id','name']

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display=['id','name']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display=['id','name','pic']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','maincategory','subcategory','brand','color','size','baseprice','discount','finalprice','stock','pic1','pic2']

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display=['id','name','username','email','phone','address','pin','city','state']

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display=['id','buyer','product']


@admin.register(Checkout)
class WishlistAdmin(admin.ModelAdmin):
    list_display=['id','buyer','orderstatus','paymentstatus','paymentmode','subtotal','shipping','total','date']


@admin.register(CheckoutProduct)
class CheckoutProductAdmin(admin.ModelAdmin):
    list_display=['id','checkout','product']


@admin.register(Newslatter)
class NewslatterAdmin(admin.ModelAdmin):
    list_display=['id','email']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','subject','message','date']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display=['id','name']
    