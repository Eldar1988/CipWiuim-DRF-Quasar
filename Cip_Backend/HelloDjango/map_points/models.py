from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Region(models.Model):
    title = models.CharField('Название области или региона', max_length=250)
    coordinates = models.CharField('Координаты региона', null=True, blank=True, max_length=50)
    slug = models.SlugField('Slug', unique=True,
                            help_text='только маленькие латинские буквы, без пробелов и спец символов')
    order = models.PositiveSmallIntegerField('Порядковый номер', help_text='Будет использоваться для сортировки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
        ordering = ('order',)


class PointType(models.Model):
    title = models.CharField('Название отрасли', max_length=250)
    slug = models.SlugField('Slug', unique=True, null=True, blank=True,
                            help_text='только маленькие латинские буквы, без пробелов и спец символов')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отрасль'
        verbose_name_plural = 'Отрасли'
        ordering = ('order',)


class MapPoint(models.Model):
    """Точка на карте"""
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('Slug', unique=True)
    type = models.ManyToManyField(PointType, blank=True,
                                  verbose_name='Отрасль', related_name='points')
    region = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name='Область или регион',
                               related_name='points')
    coordinates = models.CharField('Координаты', null=True, blank=True, max_length=50)
    image = models.URLField('Изображение', null=True, blank=True)
    description = RichTextUploadingField('Полное описание')
    pub_date = models.DateField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объект на карте'
        verbose_name_plural = 'Объекты на карте'


class MapPointImage(models.Model):
    map_point = models.ForeignKey(MapPoint, on_delete=models.SET_NULL, null=True, blank=True, related_name='images')
    image = models.URLField('Ссылка на картинку')
    order = models.PositiveSmallIntegerField('Порядковый номер')

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ('order',)


class MapPointVideo(models.Model):
    map_point = models.ForeignKey(MapPoint, on_delete=models.SET_NULL, null=True, blank=True, related_name='videos')
    url = models.URLField('Ссылка на видео', default='https://www.youtube.com/embed/',
                          help_text='Скопировать и вставить конечный параметр ссылки после знака =')
    order = models.PositiveSmallIntegerField('Порядковый номер')

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ('order',)
