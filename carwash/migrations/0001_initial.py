# Generated by Django 4.0.5 on 2023-04-03 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CallApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('phone_number', models.CharField(max_length=16, verbose_name='Номер телефона')),
                ('msg', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('description', models.TextField(blank=True, default='', verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('car_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carclass', verbose_name='Класс')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carwash.service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
                'ordering': ('service', 'car_class'),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_payed', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('status', models.IntegerField(choices=[(0, 'Не выполнено'), (1, 'Выполнено'), (2, 'Отменено')], default=0, verbose_name='Состояние')),
                ('payed_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата оплаты')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car', verbose_name='Авто')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Клиент')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carwash.price', verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
