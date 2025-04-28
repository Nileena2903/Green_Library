
from django.urls import path
from . import views


urlpatterns = [
 path('',views.ReadData),
 path('OneData/<int:pk>',views.OneData),
 path('postdata',views.PostData),
 path('UpdateAll/<int:pk>',views.UpdateData),
 path('UpdateOne/<int:pk>',views.UpdateOne),
 path('DeleteData/<int:pk>',views.DeleteData),
]

