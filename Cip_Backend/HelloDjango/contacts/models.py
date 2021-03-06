from django.db import models


class Contact(models.Model):
    """Контактная информация"""
    address = models.TextField('Адрес компании')
    email = models.EmailField('Email')
    phone = models.CharField('Телефон компании', max_length=20)
    whatsapp = models.CharField('Whatsapp', max_length=20, help_text='В формате: 7707855****')

    def __str__(self):
        return 'Контакты'

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'


class SocialNetwork(models.Model):
    """Социальные сети"""
    title = models.CharField('Название сети', max_length=255)
    icon = models.CharField('Иконка', default='mdi-', max_length=255,
                            help_text='Искать на сайте https://materialdesignicons.com/')
    url = models.URLField('Ссылка на профиль в сети')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'


class Bot(models.Model):
    target = models.CharField('Предназначение', max_length=100)
    name = models.CharField('Имя бота', max_length=200)
    token = models.CharField(max_length=255)
    chat_id = models.BigIntegerField('Чат id')
    create_date = models.DateTimeField('Создан', auto_now_add=True)

    def __str__(self):
        return self.target

    class Meta:
        verbose_name = 'Бот'
        verbose_name_plural = 'Боты'


class CallBack(models.Model):
    """Заявка на консультацию"""
    name = models.CharField('Имя', max_length=255)
    phone = models.CharField('Телефон', max_length=20)
    note = models.TextField('Заметка', null=True, blank=True)
    complete = models.BooleanField('Обработана', default=False)
    date = models.DateTimeField('Дата', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки на консультацию'
        ordering = ('-date',)

