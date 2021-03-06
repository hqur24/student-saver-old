from django.urls import path
from . views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView,
                    PostSubjectView)
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', PostListView.as_view(), name ='blog-home' ),
    path('user/<str:username>', UserPostListView.as_view(), name ='user-posts' ),
    path('subject/<str:subject>', PostSubjectView.as_view(), name ='subject-posts' ),
    path('post/<int:pk>/', PostDetailView.as_view(), name ='post-detail' ),
    path('post/new/', PostCreateView.as_view(), name ='post-create' ),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name ='post-update' ),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name ='post-delete' ),
    path('resources/', views.resources, name='blog-resources'),
]
