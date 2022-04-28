from rest_framework import serializers
from .models import Article, Comment


class FilterCommentListSerializer(serializers.ListSerializer):
    """Фильтр комментариев"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super(FilterCommentListSerializer, self).to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Рекурсивный вывод комментариев"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class RecursiveThirdLevelSerializer(serializers.Serializer):
    """Рекурсивный вывод комментариев до 3-ого уровня вложенности"""

    def to_representation(self, value):
        if value.level < 3:
            serializer = self.parent.parent.__class__(
                value, context=self.context)
            return serializer.data
        else:
            return None


class CommentThirdLevelSerializer(serializers.ModelSerializer):
    """Вывод комментариев"""
    children = RecursiveThirdLevelSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ['id', 'parent', 'nickname', 'email',
                  'text_comment', 'pub_date', 'level', 'children']


class CommentCreateSerializer(serializers.ModelSerializer):
    """Добавления нового комментария"""

    class Meta:
        model = Comment
        fields = ['article', 'parent', 'nickname', 'email', 'text_comment']


class CommentDetailSerializer(serializers.ModelSerializer):
    """Вывод детальной информации о комментарии и его children"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ['id', 'parent', 'nickname', 'email',
                  'text_comment', 'pub_date', 'level', 'children']


class ArticleCreateSerializer(serializers.ModelSerializer):
    """Добавления новой статьи"""

    class Meta:
        model = Article
        fields = ['name_article', 'text_article']


class ArticleSerializer(serializers.ModelSerializer):
    """Вывод всех статей"""
    class Meta:
        model = Article
        fields = ['id', 'name_article', 'date']


class ArticleDetailSerializer(serializers.ModelSerializer):
    """Вывод детальной информации о статье и комментарии"""
    comments = CommentThirdLevelSerializer(many=True)

    class Meta:
        model = Article
        fields = ['name_article', 'text_article', 'date', 'comments']
