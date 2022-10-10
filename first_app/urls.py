from django.urls import path
from  . import views

urlpatterns = [
    # for registration to driver
    path('', views.form1),
    path('reg',views.reg),
    path('driver',views.driver),

    # for registration to police
    path('regp',views.police),
    path('police',views.regpolice),

    # for login to User
    path('login',views.login),
    path('signin',views.signin),

    
]
