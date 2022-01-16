from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.home, name="home"),
	path('store', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('shopping_cart/', views.shopping_cart, name="shopping_cart"),
	path('checkout/', views.shopping_checkout, name="checkout"),
	path('contact/', views.contact, name="contact"),
	path('menu/', views.menu, name="menu"),
	path('gallery/', views.gallery, name="gallery"),
	path('shop/', views.shop, name="shop"),
	path('fundraising/', views.fundraising, name="fundraising"),
	path('login/', views.login, name="login"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]