from django.urls import path
from . import views

urlpatterns = [
  path('',views.home,name='home'),
  path('upload/', views.upload_video, name='upload_video'), 
  path('livedetect/',views.livedetect,name='live_detect'),
  path('upload_i/',views.upload_image,name='upload_i')
]