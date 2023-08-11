"""
URL configuration for supershop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainApp import views as mainApp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainApp.homePage,name='home'),
    path('about/',mainApp.aboutPage,name="about"),
    path('cart/',mainApp.cartPage,name="cart"),
    path('delete-cart/<str:id>/',mainApp.deleteCartPage,name="delete-cart"),
    path('update-cart/<str:id>/<str:op>/',mainApp.updateCartPage,name="update-cart"),
    path('add-to-cart/',mainApp.addToCartPage,name="add-to-cart"),
    path('checkout/',mainApp.checkoutPage,name="checkout"),
    path('payment-success/',mainApp.paymentSuccessPage,name="payment-success"),
    path('re-payment/<int:id>/',mainApp.rePayment,name="re-payment"),
    path('confirmation/',mainApp.confirmationPage,name="confirmation"),
    path('contact/',mainApp.contactPage,name="contact"),
    path('login/',mainApp.loginPage,name="login"),
    path('logout/',mainApp.logoutPage,name="logout"),
    path('profile/',mainApp.profilePage,name='profile'),
    path('signup/',mainApp.signupPage,name="signup"),
    path('update-profile/',mainApp.updateProfile,name="update-profile"),
    path('shop/<str:mc>/<str:sc>/<str:br>/',mainApp.shopPage,name="shop"),
    path('single-product/<int:id>/',mainApp.single_productPage,name="single-product"),
    path('add-to-wishlist/<int:id>/',mainApp.addToWishlistPage,name='add-to-wishlist'),
    path('delete-wishlist/<int:id>/',mainApp.deleteWishlistPage,name='delete-wishlist'),
    path('newslatter/subscribe/',mainApp.newslatterSubscribePage,name='newslatter-subscribe'),
    path('search/',mainApp.searchPage,name='search'),
    path('forget-password-1/',mainApp.forgetPassword1Page,name='forget-password-1'),
    path('forget-password-2/',mainApp.forgetPassword2Page,name='forget-password-2'),
    path('forget-password-3/',mainApp.forgetPassword3Page,name='forget-password-3'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
