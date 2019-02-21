from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("children/", views.children, name='children'),
    path("moms/", views.moms, name="moms"),
    path("addchild/", views.addChild, name="add"),
    path("deletemom/", views.deleteMom, name="delete")



]