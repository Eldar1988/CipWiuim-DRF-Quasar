# Generated by Django 3.1.4 on 2020-12-30 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20201230_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='public',
            field=models.BooleanField(default=False, verbose_name='Опубликовать'),
        ),
    ]
