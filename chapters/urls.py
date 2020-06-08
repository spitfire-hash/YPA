from django.urls import path
from . import views

app_name = 'chapters'

urlpatterns = [
    path('', views.home, name='home'),
    path('view-chapters/', views.view_chapters, name="view-chapters")
]
