# Generated by Django 3.1.4 on 2020-12-17 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email (необязательно)'),
        ),
    ]
