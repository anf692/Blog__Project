from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),  
    path('form', views.ajout_post, name='formulaire'),  
    path('list', views.post_list, name='post_list'),
    path('posts/<int:id>', views.post_detail, name='post_detail'),
    path('delete/<int:id>', views.delete, name='supprimer'),

]