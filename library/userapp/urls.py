from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('signup',views.signup),
    path('viewbooks',views.viewbooks),
    path('addbook',views.addbook),
    path('searchbooks',views.searchbooks),
    path('addpen',views.addpen),
    path('viewpens',views.viewpens),
    path('addcart/<int:pk>',views.addcart,name='cart'),
     path('viewform',views.viewform),
]