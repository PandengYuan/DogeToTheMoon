from django.urls import path
from django.conf.urls import url
from rango import views

app_name = 'rango'

urlpatterns = [

    #homepage
    path('', views.index, name='index'),
    #display different category page
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    #add a new category page
    path('add_category/', views.add_category, name='add_category'),
    #show the detail of a product  page
    path('product/<slug:product_name_slug>/', views.show_product, name='show_product'),
    #sign in page
    path('register/', views.register, name='register'),
    #login page
    path('login/', views.user_login, name='login'),
    #used to determine the correctness of login
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
    # the my account page of the user whose type is buyer
    path('buyer-my-account/', views.buyer_my_account, name='buyer_my_account'),
    #the page showa the cart of a 'buyer' user
    path('cart/', views.cart, name='cart'),
    #the paymennt page of a 'buyer' user
    path('payment/', views.payment, name='payment'),
    #the my account page of 'seller' user
    path('seller-my-account/', views.seller_my_account, name='seller_my_account'),
    #the page used to upload a product, which is only can be accessed by the 'seller' user
    path('upload-product/', views.upload_product, name='upload_product'),
    #the page used to remove a product, which is only can be accessed by the 'seller' user
    path('remove-product/', views.remove_product, name='remove_product'),
    #the search functionality for the app
    path('product-search/', views.product_search, name='product_search'),
]