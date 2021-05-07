# Generated by Django 3.1.4 on 2021-05-07 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map_points', '0006_region_coordinates'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapPointVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(default='https://www.youtube.com/embed/', help_text='Скопировать и вставить конечный параметр ссылки после знака =', verbose_name='Ссылка на видео')),
                ('order', models.PositiveSmallIntegerField(verbose_name='Порядковый номер')),
                ('map_point', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='videos', to='map_points.mappoint')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='MapPointImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(verbose_name='Ссылка на картинку')),
                ('order', models.PositiveSmallIntegerField(verbose_name='Порядковый номер')),
                ('map_point', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='map_points.mappoint')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
                'ordering': ('order',),
            },
        ),
    ]