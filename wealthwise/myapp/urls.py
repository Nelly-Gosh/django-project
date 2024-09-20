from django.urls import path
from . import views 

urlpatterns = [
path('',views.home,name="home"),
path('about/',views.about,name="about"),
path('contact/',views.contact,name="contact"),
path('invest/',views.invest,name="investment"),
path('services/',views.services,name="services"),
path('login/',views.login,name="login"),
path('signup/',views.signup,name="signup"),
path('Dashboard/', views.dashboard, name='Dashboard'),
path('reinvest/',views.reinvest,name="reinvest"),
path('deposit/',views.deposit,name="deposit"),
path('withdraw/',views.withdraw,name="withdraw"),
path('transactions/',views.transactions,name="transactions"),
]