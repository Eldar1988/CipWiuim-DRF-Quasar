from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Region(models.Model):
    title = models.CharField('Название области или региона', max_length=250)
    slug = models.SlugField('Slug', unique=True,
                            help_text='только маленькие латинские буквы, без пробелов и спец символов')
    order = models.PositiveSmallIntegerField('Порядковый номер', help_text='Будет использоваться для сортировки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
        ordering = ('order',)


class MapPoint(models.Model):
    """Точка на карте"""
    title = models.CharField('Заголовок', max_length=200)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name='Область или регион',
                               related_name='points')
    x = models.FloatField('Координата Х', null=True)
    y = models.FloatField('Координата y', null=True)
    map_title = models.CharField('Заголовок для объекта на карте (необязательно)', max_length=200, blank=True)
    short_description = RichTextUploadingField('Краткое описание', help_text='Будет отображаться на карте')
    description = RichTextUploadingField('Полное описание')
    slug = models.SlugField('Slug', unique=True)
    pub_date = models.DateField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объект на карте'
        verbose_name_plural = 'Объекты на карте'
