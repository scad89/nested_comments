from django.urls import path
from . import views


urlpatterns = [
    path('create_article/', views.ArticleCreateAPIView.as_view(),
         name='create_article'),
    path('articles/', views.GetArticlesListView.as_view(), name='articles'),
    path("article/<int:pk>/", views.GetArticleDetailRetrieveAPIView.as_view(),
         name='detail_article'),
    path('create_comment/', views.NewCommentCreateAPIView.as_view(),
         name='create_comments'),
    path("comment/<int:pk>/", views.GetCommentDetailRetrieveAPIView.as_view(),
         name='detail_comment')
]
