from django.urls import path
from .views import (
    postListView,
    postDetailView,
    postCreateView,
    postUpdateView,
    postDeleteView,
    UserpostListView,
)
from . import views

urlpatterns = [
    path("", postListView.as_view(), name="blog-home"),
    path("post/<int:pk>/", postDetailView.as_view(), name="post-detail"),
    path("user/<str:username>/", UserpostListView.as_view(), name="user-posts"),
    path("post/new/", postCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", postUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", postDeleteView.as_view(), name="post-delete"),
    path("about/", views.about, name="blog-about"),
]
