from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RegisterView, ProfileView, NoteViewSet, login_view


router = DefaultRouter()
router.register('notes', NoteViewSet, basename='notes')


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', include(router.urls)),
]