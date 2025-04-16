from django.urls import path
from .views import *

urlpatterns = [
  path('', profile_view, name='profile'),  # Profile page URL
  path('edit/', profile_edit_view, name='profile-edit'),  # Profile edit page URL
]