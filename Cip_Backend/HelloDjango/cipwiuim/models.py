from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class HomePage(models.Model):
    """Home page seo info"""
    title = models.CharField('Title сайта', max_length=110)
    description = models.TextField('Описание сайта', max_length=190)
    logo = models.URLField('Ссылка на лого сайта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Главная страница СЕО'
        verbose_name_plural = 'Главная страцниа СЕО'


class SliderSlide(models.Model):
    """Slide for home Slider"""
    title = models.CharField('Заголовок слайда', max_length=70)
    text = models.TextField('Текст на слайдере')
    image = models.URLField('Ссылка на изображение')
    button_text = models.CharField('Текст на кнопке', max_length=50)
    button_url = models.CharField('Ссылка кнопки', max_length=255, null=True, blank=True)
    order = models.PositiveSmallIntegerField('Порядковый номер слайда')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайдер'
        ordering = ('order',)


class CIPAbout(models.Model):
    """О компании CIP WIUIM"""
    title = models.CharField('Заголовок', default='CipWiuim', max_length=255, db_index=True)
    description = models.TextField('Краткое описание')
    bio = RichTextUploadingField('Полное описание компании')
    logo = models.URLField('Ссылка на изображение (логотип)')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация о компании'
        verbose_name_plural = 'Информация о компании'


class CIPReview(models.Model):
    """Отзывы о CIP WIUIM"""
    name = models.CharField('Имя', max_length=255)
    text = models.TextField('Текст отзыва или мнения')
    position = models.CharField('Дополнительно', max_length=100, help_text='Например: должность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв или мнение'
        verbose_name_plural = 'Отзывы и мнения'


class CIPPartner(models.Model):
    """Партнеры CIP WIUIM"""
    title = models.CharField('Название компании-партнера', max_length=100)
    logo = models.URLField('Логотип партнера (ссылка на лого)')
    url = models.URLField('Ссылка на сайт партнера')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'


class CIPPartnerForm(models.Model):
    """Формы сотрудничества с CIP WIUIM"""
    title = models.CharField('Заголовок', max_length=100)
    short_description = models.TextField('Краткое описание',
                                         help_text='Будет выводится на главной странице')
    description = RichTextUploadingField('Полное описание')
    image = models.URLField('Ссылка на картинку')
    banner = models.URLField('Ссылка на баннер', blank=True, null=True)
    banner_title = models.CharField('Заголовок на баннере', max_length=100, blank=True, null=True)
    slug = models.SlugField('Slug', unique=True)
    order = models.PositiveSmallIntegerField('Порядковый номер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Форма партнерства'
        verbose_name_plural = 'Формы партнерства'
        ordering = ('order',)


class PartnerFile(models.Model):
    """Файлы для партнеров"""
    partner_form = models.ForeignKey(CIPPartnerForm, on_delete=models.SET, null=True, blank=True,
                                     verbose_name='Форма партнества', related_name='files')
    title = models.CharField('Название файла', max_length=255)
    url = models.URLField('Ссылка на файл')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Файл для партнеров'
        verbose_name_plural = 'Файлы для партнеров'


class ForPartnerNotification(models.Model):
    """Уведомления для партнеров"""
    partner_form = models.ForeignKey(CIPPartnerForm, on_delete=models.SET_NULL, null=True, blank=True,
                                     verbose_name='Форма партнерства', related_name='notifications')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Пользователь', related_name='notifications')
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст уведомления')
    pub_date = models.DateTimeField('Дата создания уведомления', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Уведомление для партнера'
        verbose_name_plural = 'Уведомления для партнеров'
        ordering = ('-pub_date',)


class NotificationFile(models.Model):
    """Файлы для уведомлений"""
    notification = models.ForeignKey(ForPartnerNotification, on_delete=models.SET, null=True, blank=True,
                                     verbose_name='Уведомление', related_name='files')
    title = models.CharField('Название файла', max_length=255)
    url = models.URLField('Ссылка на файл')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Файл к уведомлению'
        verbose_name_plural = 'Файлы к уведомлениям'


class CIPQuestionAnswer(models.Model):
    """Вопросы и ответы"""
    question = models.CharField('Вопрос', max_length=255)
    answer = models.TextField('Ответ')
    order = models.PositiveSmallIntegerField('Порядковый номер', help_text='Необходим для сортировки вопросов')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос и ответ'
        verbose_name_plural = 'Вопросы и ответы'
        ordering = ('order',)


class Rule(models.Model):
    """Правила пользования сайтом"""
    title = models.CharField('Заголовок', max_length=255, db_index=True,
                             help_text='Указать для кого правила. Например: общие или для инвесторов')
    description = RichTextUploadingField('Полное описание')
    slug = models.SlugField('Slug', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Правило пользования сайтом'
        verbose_name_plural = 'Правила пользования сайтом'


class CIPPhoto(models.Model):
    """Фотогалерея"""
    title = models.CharField('Название фото', max_length=255, db_index=True)
    url = models.URLField('Ссылка на фото')
    order = models.PositiveSmallIntegerField('Порядковый номер', help_text='Будет использоваться для сортировки')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотогалерея'
        ordering = ('order',)


class CIPVideo(models.Model):
    """Видео галерея"""
    title = models.CharField('Название видео', max_length=255, db_index=True)
    url = models.URLField('Ссылка на видео', default='https://www.youtube.com/embed/',
                          help_text='Скопировать и вставить конечный параметр ссылки после знака =')
    order = models.PositiveSmallIntegerField('Порядковый номер', help_text='Будет использоваться для сортировки')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видеогалерея'
        ordering = ('order',)