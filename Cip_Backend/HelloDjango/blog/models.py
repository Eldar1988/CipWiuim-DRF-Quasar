from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    """Категория"""
    title = models.CharField('Заголовок', max_length=255, db_index=True)
    description = models.TextField('Краткое описание категории')
    slug = models.SlugField('Slug', unique=True,
                            help_text='только маленькие латинские буквы, без пробелов и спец символов')
    order = models.PositiveSmallIntegerField('Порядковый номер', help_text='Будет использоваться для сортировки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('order',)


class Post(models.Model):
    """Пост"""
    title = models.CharField('Заголовок', max_length=255, db_index=True)
    description = models.TextField('Краткое описание поста')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True,
                                 verbose_name='Категория поста', related_name='posts')
    image = models.URLField('Изображение')
    body = RichTextUploadingField('Тело поста')
    rating = models.PositiveSmallIntegerField('Рейтинг поста от 1 до 10', default=10)
    future = models.BooleanField('Рекомендовать', default=False)
    public = models.BooleanField('Опубликовать', default=False)
    order = models.PositiveSmallIntegerField('Порядковый номер', help_text='Будет использоваться для сортировки')
    slug = models.SlugField('Slug', unique=True,
                            help_text='только маленькие латинские буквы, без пробелов и спец символов')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)
    views = models.PositiveSmallIntegerField('Количество просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('order',)


class Comment(models.Model):
    """Комментарий к посту"""
    email = models.EmailField()
    name = models.CharField('Имя автора комментария', max_length=100)
    text = models.TextField('Комментарий')
    parent = models.ForeignKey('self', verbose_name='Ответ на комментарий', on_delete=models.SET_NULL,
                               blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, related_name='comments', verbose_name='Пост',
                             blank=True, null=True )
    public = models.BooleanField('Опубликовать', default=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.post

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-pub_date',)


class PostPhoto(models.Model):
    """Фото к посту"""
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Пост', related_name='images')
    title = models.CharField('Название фото', max_length=255, db_index=True)
    url = models.URLField('Ссылка на фото')
    order = models.PositiveSmallIntegerField('Порядковый номер', help_text='Будет использоваться для сортировки')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото к посту'
        verbose_name_plural = 'Фото к постам'
        ordering = ('order',)
