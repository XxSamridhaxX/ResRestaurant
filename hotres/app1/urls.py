app_name="app1"
from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.customer_list, name='customer_list'),
    path("register/",views.CustomerRegistrationView.as_view(), name="home"),
    path('login/', views.CustomerLoginView.as_view(), name='customer_login'),
    # path('home/',views.homepage,name="home"),
    path('profile/', views.UserProfileView.as_view(), name='userprofile_'),
]
