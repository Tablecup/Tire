# Generated by Django 4.0.5 on 2022-06-18 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carwash', '0003_alter_callapplication_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата оформления'),
        ),
    ]
