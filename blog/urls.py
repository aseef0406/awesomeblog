from django.urls import path
from . import views


urlpatterns=[
    path('',views.IndexViews.as_view(),name='home'),
    path('article/<int:pk>/',views.PostDetailView.as_view(),name="post-detail"),
    path('article/new',views.CreatePostView.as_view(),name="post-new"),
    path('article/edit/<int:pk>/',views.PostEditView.as_view(),name="post-edit"),
    path('article/delete/<int:pk>',views.PostDeleteView.as_view(),name="post-delete"),
]