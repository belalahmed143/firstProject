from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
from .views import home,login,signup,logout,cart,checkout
urlpatterns = [
    path('', home.Index.as_view(), name='index'),
    path("signup/", signup.Registration.as_view(), name="signup"),
    # path("signup/", views.signup, name="signup"),
    # path("signin/", views.signin, name="signin"),
    path("signin/",login.Login.as_view(), name='signin'),
    path('logout',logout.logout, name='logout'),
    path('cart/',cart.Cart.as_view(), name='cart'),
    path('check-out/',checkout.CheckOut.as_view(), name='check-out')
]