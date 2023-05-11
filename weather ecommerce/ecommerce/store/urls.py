from django.urls import path, include
from . import views

from store.views import my_api_view 


urlpatterns = [
    path('' , views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name ="checkout"),
    path('update_item/', views.updateItem, name ="update_item"),
    path('submit_output/', views.submit_output, name='submit_output'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('api/mydata/', my_api_view, name='my_api_view'),

    path('login/' , views.login_view, name="login_view"),
    path('logout/' , views.log_out, name="log_out"),
    path('signup/' , views.sign_up, name="signup"),
    # path('login/signup.html/login.html/' , views.login, name="login1")
]

