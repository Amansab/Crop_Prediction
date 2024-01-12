from django.urls import path
from .import views

urlpatterns=[
    path('index.html',views.index,name="index"),
    path('login.html',views.login,name="login"),
    path('register.html',views.register,name="register"),
    path('logout',views.logout,name='logout'),
    path('pricing.html', views.pricing,name="pricing"),
    path("contacts.html",views.contacts,name="contacts"),
    path("authenticate.html",views.authenticate,name="authenticate"),
    path("test.html",views.predictor,name="predictor"),
    path('predictor',views.predictor, name="predictor"),
    path('result',views.test1,name='result')
]