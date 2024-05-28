# urls.py
from django.urls import path
from .views import RegisterView, LoginView, LogoutView, FileUploadView, NameURLView, CamDetectView

urlpatterns = [
  # path('admin/', admin.site.urls),
  path('register/', RegisterView.as_view(), name='register'),
  path('login/', LoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path('upload_file/', FileUploadView.as_view(), name='upload_file'),
  path('data/', NameURLView.as_view(), name='data'),
  path('cam_detect/<int:pk>/', CamDetectView.as_view(), name='cam_detect'),
]

# {
#     "username": "test1",
#     // "email":"jitendralohani01@gmail.com",
#     "password": "testpassword"
#     // "password2": "testpassword"
# }