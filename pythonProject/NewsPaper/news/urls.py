from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, SearchList

urlpatterns = [
    path('news/', PostsList.as_view(), name = 'post_list'),
    path('news/<int:pk>', PostDetail.as_view(), name = 'news_detail'),
    path('news/search/', SearchList.as_view(), name = 'search_list'),
    path('news/create/', PostCreate.as_view(), name = 'post_create'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('articles/<int:pk>', PostDetail.as_view(), name = 'articles_detail'),
    path('articles/create/', PostCreate.as_view(), name = 'post_create'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]