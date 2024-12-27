from django.urls import path
from . import views

urlpatterns = [
    path("index/",views.index,name='index'),
    path("<int:id>",views.view_profile,name="view_profile"),
    path("edit/<int:id>/",views.edit,name="edit"),
    path("profile/",views.profile,name='profile'),
    path("",views.login_view,name='login'),
    path("registration/",views.register_view,name='registration')

]