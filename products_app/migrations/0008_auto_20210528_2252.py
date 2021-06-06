# Generated by Django 2.2.23 on 2021-05-28 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0007_auto_20210528_2156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='orderedproducts',
            options={'verbose_name': 'Заказанный товар', 'verbose_name_plural': 'Заказанные товары'},
        ),
        migrations.AlterField(
            model_name='orderedproducts',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_app.Product', verbose_name='Товары'),
        ),
    ]
