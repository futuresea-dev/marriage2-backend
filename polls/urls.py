from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('invite_request', views.invite_request, name='invite_request'),
    path('my_invites', views.my_invites, name='my_invites'),
    path('uploadImage', views.uploadImage, name="uploadImage"),
    path('updateUserProfile', views.updateUserProfile, name="updateUserProfile"),
    path('login', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)