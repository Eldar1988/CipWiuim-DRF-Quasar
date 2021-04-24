from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from companies.models import Profile, Company


class Project(models.Model):
    """Проект"""
    project_admin = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True,
                                      verbose_name='Администратор проекта', related_name='projects')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Компания', related_name='projects')
    title = models.CharField('Название проекта', max_length=255, db_index=True)
    slug = models.SlugField('Slug', unique=True,
                            help_text='только маленькие латинские буквы, без пробелов и спец символов')
    description = models.TextField('Краткое описание (отображается в списке)',
                                   help_text='Будет отображено в общих списках проектов, а также в теге description')
    short_description = RichTextUploadingField('Краткое описание проекта (отображается на странице проекта)')
    bio = RichTextUploadingField('Полное описание проекта')
    image = models.URLField('Картинка проекта')
    order = models.PositiveSmallIntegerField('Порядковый номер проекта',
                                             help_text='Необходим для сортировки проектов в списках')
    public = models.BooleanField('Опубликовать', default=False)
    pub_date = models.DateTimeField('Дата публикации проекта', auto_now_add=True)
    update = models.DateTimeField('Изменения', auto_now=True)
    views = models.PositiveSmallIntegerField('Количество просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ('order',)


class DigitalIndicator(models.Model):
    """Цифровой показатель проекта"""
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Проект', related_name='indicators')
    title = models.CharField('Заголовок показателя', max_length=255, db_index=True)
    value = models.CharField('Значение показателя', max_length=30, help_text='Например: 80%')
    max_value = models.CharField('Макимально возможное значение', max_length=30, help_text='Например: 100%')
    order = models.PositiveSmallIntegerField('Порядковый номер', help_text='Будет использоваться для сортировки')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цифровой показатель проекта'
        verbose_name_plural = 'Цифровые показатели проектов'
        ordering = ('order',)


class Benefit(models.Model):
    """Преимущество проекта"""
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Проект', related_name='benefits')
    title = models.CharField('Заголовок', max_length=100, db_index=True)
    text = models.TextField('Описание')
    icon = models.CharField('Иконка', max_length=100, default='mdi-', help_text='Смотреть на сайте https://materialdesignicons.com/')
    order = models.PositiveSmallIntegerField('Порядковый номер', help_text='Будет использоваться для сортировки')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущество проекта'
        verbose_name_plural = 'Преимущества проектов'
        ordering = ('order',)


class Structure(models.Model):
    """Структура проекта"""
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Проект', related_name='structures')
    title = models.CharField('Заголовок', max_length=255)
    slug = models.SlugField('Slug', unique=True,
                            help_text='только маленькие латинские буквы, без пробелов и спец символов')
    description = RichTextUploadingField('Краткое описание')
    seo_description = RichTextUploadingField('Краткое описание (для СЕО)', help_text='Может дублировать краткое описание')
    miniature = models.URLField('Миниатюра (ссылка на изображение)')
    image = models.URLField('Изображение проекта')
    bio = RichTextUploadingField('Полное описание')
    order = models.PositiveSmallIntegerField('Порядковый номер', help_text='Будет использоваться для сортировки')
    public = models.BooleanField('Опубликовать', default=False)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Структура проекта'
        verbose_name_plural = 'Структуры проектов'
        ordering = ('order',)


class QuestionAndAnswer(models.Model):
    """Вопрос и ответ"""
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Проект', related_name='questions')
    question = models.CharField('Вопрос', max_length=255, db_index=True)
    answer = models.TextField('Ответ')
    order = models.PositiveSmallIntegerField('Порядковый номер', help_text='Будет использоваться для сортировки')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос и ответ'
        verbose_name_plural = 'Вопросы и ответы'
        ordering = ('order',)


class Review(models.Model):
    """Отзыв о проекте"""
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Проект', related_name='reviews')
    name = models.CharField('Имя', max_length=255, db_index=True)
    text = models.TextField('Отзыв')
    professional = models.CharField('Профессия', max_length=255)
    avatar = models.URLField('Аватар (ссылка на изображение) необзятелно', blank=True, null=True)
    order = models.PositiveSmallIntegerField('Порядковый номер', help_text='Будет использоваться для сортировки')
    public = models.BooleanField('Опубликовать', default=False)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв о проекте'
        verbose_name_plural = 'Отзывы о проектах'
        ordering = ('order',)


class ProjectVideo(models.Model):
    """Видео проекта"""
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Проект', related_name='videos')
    title = models.CharField('Название видео', max_length=255, db_index=True)
    url = models.URLField('Ссылка на видео', default='https://www.youtube.com/embed/',
                          help_text='Скопировать и вставить конечный параметр ссылки после знака =')
    order = models.PositiveSmallIntegerField('Порядковый номер', help_text='Будет использоваться для сортировки')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео о проекте'
        verbose_name_plural = 'Видео о проектах'
        ordering = ('order',)


class ProjectPhoto(models.Model):
    """Фото проекта"""
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Проект', related_name='photos')
    title = models.CharField('Название фото', max_length=255, db_index=True)
    url = models.URLField('Ссылка на фото')
    order = models.PositiveSmallIntegerField('Порядковый номер', help_text='Будет использоваться для сортировки')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото к проекту'
        verbose_name_plural = 'Фото к проектам'
        ordering = ('order',)


class ProjectFile(models.Model):
    """Файл проекта"""
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Проект', related_name='files')
    title = models.CharField('Название файла', max_length=255, db_index=True)
    url = models.URLField('Ссылка на файл')
    order = models.PositiveSmallIntegerField('Порядковый номер', help_text='Будет использоваться для сортировки')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Файл к проекту'
        verbose_name_plural = 'Файлы к проектам'
        ordering = ('order',)


