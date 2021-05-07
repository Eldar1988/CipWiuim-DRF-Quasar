# Generated by Django 3.1.4 on 2021-05-07 03:02

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cipwiuim', '0007_cippartnerform_register_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Главная страница', 'verbose_name_plural': 'Главная страница'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='blog_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание (блог)'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='forum_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание (форум)'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='map_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание (карта)'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='projects_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание (проекты)'),
        ),
    ]