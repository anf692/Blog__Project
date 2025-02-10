from django.urls import path
from blog import views

urlpatterns = [
path('form', views.ajout_post, name='formulaire'),  
path('', views.post_list, name='post_list'),
path('posts/<int:id>', views.post_detail, name='post_detail'),
]