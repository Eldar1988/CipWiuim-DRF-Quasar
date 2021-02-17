from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from companies.models import Profile
from projects.models import Project


class Theme(models.Model):
    """Тема форума"""
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='Автор темы', related_name='themes')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Проект', related_name='forum_themes')
    title = models.CharField('Заголовок', max_length=255, db_index=True)
    description = models.TextField('Краткое описание темы')
    body = RichTextUploadingField('Тема')
    order = models.PositiveSmallIntegerField('Порядковый номер', help_text='Будет использоваться для сортировки')
    slug = models.SlugField('Slug', unique=True,
                            help_text='только маленькие латинские буквы, без пробелов и спец символов')
    public = models.BooleanField('Опубликовать', default=False)
    views = models.PositiveSmallIntegerField('Количество просмотров', default=0)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тема форума'
        verbose_name_plural = 'Темы форума'
        ordering = ('order',)


class Answer(models.Model):
    """Ответ"""
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='Тема', related_name='answers')
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Профиль автора сообщения', related_name='answers')
    email = models.EmailField(null=True, blank=True)
    name = models.CharField('Имя автора', max_length=255, null=True, blank=True)
    text = models.TextField('Сообщение', max_length=7000)
    answer_for = models.ForeignKey('self', verbose_name='Ответ на сообщение от', on_delete=models.SET_NULL,
                                   blank=True, null=True, related_name='child')
    public = models.BooleanField('Опубликовать', default=True)
    pub_date = models.DateTimeField('Дата публикации',auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ('-pub_date',)
