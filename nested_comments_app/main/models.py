from wsgiref.simple_server import demo_app
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Article(models.Model):
    """Статья"""
    name_article = models.CharField(max_length=50, default='title')
    text_article = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_article

    class MPTTMeta:
        order_insertion_by = ['name_article']

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Comment(MPTTModel):
    """Комментарий"""
    article = models.ForeignKey(
        Article, on_delete=models.DO_NOTHING, related_name='comments')
    parent = TreeForeignKey(
        'self',
        default=None,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='children')
    nickname = models.CharField(max_length=15, default='nickname')
    email = models.EmailField()
    text_comment = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nickname}, {self.email} {self.pub_date}'

    class MPTTMeta:
        order_insertion_by = ['article']

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
