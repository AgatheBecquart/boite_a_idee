from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('idea_list/', views.IdeaListView.as_view(),name='idea_list'),
    path('my_idea_list/', views.MyIdeaListView.as_view(),name='my_idea_list'),
    path('idea_detail/<int:pk>', views.IdeaDetailView.as_view(), name='idea_detail'),
    path('idea_create/', views.IdeaCreateView.as_view(), name='idea_create'),
    path('idea_update/<int:pk>', views.IdeaUpdateView.as_view(), name='idea_update'),
    path('idea_delete/<int:pk>', views.IdeaDeleteView.as_view(), name='idea_delete'),
    path('like_or_dislike/<int:pk>/', views.like_or_dislike, name='like_or_dislike'),
    path('idea_chart/', views.idea_chart, name='idea_chart'),
]