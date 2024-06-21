from django.urls import path
from .views import ImageUploadView, ImageTextListView

urlpatterns = [
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
    path('images/', ImageTextListView.as_view(), name='image-list'),
]