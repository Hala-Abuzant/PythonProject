from django.urls import path
from  . import views

urlpatterns = [
    # for registration to driver
    path('reg',views.reg),
    path('driver',views.driver),

    # for registration to police
    path('regp',views.police),
    path('police',views.regpolice),

    # for login to User
    path('login',views.login),
    path('signin',views.signin),
    path('policeinfo',views.policeinfo),
    # path('policeinfo_show', views.policeinfo_show),
    path('addviolation',views.addviolation),
    path('add', views.add_vio),
    path('showviolation', views.showviolation),
<<<<<<< HEAD
=======

<<<<<<< HEAD
>>>>>>> f1341fe71c2b4a556f652f8af6746a1c329fae36
=======
>>>>>>> f1341fe71c2b4a556f652f8af6746a1c329fae36
    path('home',views.home),
]
