from django.urls import path
from customer import views


urlpatterns=[
    path('all/',views.ListallView.as_view(),name='allbooks'),
    path('account/signup',views.SignUpView.as_view(),name='signup'),
    path('',views.SignInView.as_view(),name='signin'),
    path('account/signout',views.Sign_Out,name='signout'),
    path('customers/carts/add/<int:id>',views.AddToCartView.as_view(),name='addtocart'),
    path('customer/carts/items',views.CartItems.as_view(),name='cartitems'),
    path('customer/carts/items/remove/<int:id>',views.RemoveCartItem.as_view(),name='removecartitem')
]