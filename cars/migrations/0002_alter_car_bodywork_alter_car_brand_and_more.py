# Generated by Django 4.0.5 on 2022-06-20 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='bodywork',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carbodywork', verbose_name='Кузов'),
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carbrand', verbose_name='Марка'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carclass', verbose_name='Класс авто'),
        ),
        migrations.AlterField(
            model_name='car',
            name='coverage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carcoverage', verbose_name='Покрытие'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carmodel', verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='car',
            name='salon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carsalon', verbose_name='Салон'),
        ),
    ]
