from rest_framework import generics
from .models import Article, Comment
from .serializers import (
    ArticleCreateSerializer,
    ArticleSerializer,
    ArticleDetailSerializer,
    CommentCreateSerializer,
    CommentDetailSerializer
)


class ArticleCreateAPIView(generics.CreateAPIView):
    """Добавления новой статьи"""
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer


class GetArticlesListView(generics.ListAPIView):
    """Вывод всех статей"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class GetArticleDetailRetrieveAPIView(generics.RetrieveAPIView):
    """Вывод детальной информации о статье"""
    queryset = Article.objects.prefetch_related('comments')
    serializer_class = ArticleDetailSerializer
    lookup_field = 'pk'


class NewCommentCreateAPIView(generics.CreateAPIView):
    """Добавления нового комментария"""
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer


class GetCommentDetailRetrieveAPIView(generics.RetrieveAPIView):
    """Вывод одного комментарияя и его дочерних комментарикв"""
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    lookup_field = 'pk'
