from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('detail/<int:post_id>/', views.PostDetailView.as_view(), name='post_detail'),
    path('delete/<int:post_id>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('create/', views.PostCreatedView.as_view(), name='post_create'),
    path('post/update/<int:post_id>', views.PostUpdateView.as_view(), name='post_update'),

]