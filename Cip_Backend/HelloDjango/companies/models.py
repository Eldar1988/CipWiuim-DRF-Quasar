from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from cipwiuim.models import CIPPartnerForm


class Profile(models.Model):
    """Профиль пользователя"""
    partner_form = models.ForeignKey(CIPPartnerForm, on_delete=models.SET_NULL, null=True, blank=True,
                                     verbose_name='Форма партнерства', related_name='profiles')
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Пользователь на сайте')
    name = models.CharField('ФИО', max_length=255, db_index=True)
    phone = models.CharField('Телефон', max_length=30, null=True, blank=True)
    whatsapp = models.CharField('Whatsapp (необязательно)', max_length=30, blank=True, null=True)
    email = models.EmailField('Email (необязательно)', null=True, blank=True)
    bio = RichTextUploadingField('Информация о пользователе(био)', null=True, blank=True)
    professional = models.CharField('Профессия', max_length=255, null=True, blank=True)
    avatar = models.URLField('Аватар (ссылка)', null=True, blank=True)
    facebook = models.URLField('Ссылка на профиль в Facebook', null=True, blank=True)
    instagram = models.URLField('Ссылка на профиль в Instagram', null=True, blank=True)
    vkontakte = models.URLField('Ссылка на профиль в Контакте', null=True, blank=True)
    public = models.BooleanField('Опубликовать', default=False)
    register_date = models.DateTimeField('Дата регистрации на сайте', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


class Company(models.Model):
    """Компания"""
    admin_profile = models.ForeignKey(Profile, on_delete=models.PROTECT, verbose_name='Администратор компании',
                                      related_name='companies')
    title = models.CharField('Название компании', max_length=255, db_index=True)
    description = models.TextField('Краткое описание (род деятельности)')
    bio = RichTextUploadingField('Полное описание компании')
    logo = models.URLField('Логотип (ссылка)')
    requisites = RichTextUploadingField('Реквизиты компании', null=True, blank=True)
    address = models.TextField('Адрес компании')
    phone = models.CharField('Телефон', max_length=20)
    whatsapp = models.CharField('Whatsapp', max_length=20)
    email = models.EmailField('Email')
    cooperators = models.ManyToManyField(Profile, blank=True, verbose_name='Сотрудники компании',
                                         related_name='cooperators')
    facebook = models.URLField('Ссылка на профиль в Facebook', null=True, blank=True)
    instagram = models.URLField('Ссылка на профиль в Instagram', null=True, blank=True)
    vkontakte = models.URLField('Ссылка на профиль в Контакте', null=True, blank=True)
    slug = models.SlugField('Slug', unique=True,
                            help_text='только маленькие латинские буквы, без пробелов и спец символов')
    public = models.BooleanField('Опубликовать', default=False)
    register_date = models.DateTimeField('Дата регистрации компании на сайте', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
