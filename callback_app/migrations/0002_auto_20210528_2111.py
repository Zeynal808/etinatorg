# Generated by Django 2.2.23 on 2021-05-28 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callback_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='callback',
            options={'verbose_name': 'Запрос на обратный звонок', 'verbose_name_plural': 'Запросы на обратные звонки'},
        ),
    ]
