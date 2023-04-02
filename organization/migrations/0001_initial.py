# Generated by Django 4.0.5 on 2023-04-02 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodOfStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Срок хранения',
            },
        ),
        migrations.CreateModel(
            name='QuantityOfTires',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Количество шин',
            },
        ),
        migrations.CreateModel(
            name='TireSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Диаметр шины',
                'verbose_name_plural': 'Диаметр шин',
            },
        ),
        migrations.CreateModel(
            name='OrderStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Создан'), (1, 'Находиться на хранении'), (2, 'Отменено'), (3, 'Завершен')], default=0, verbose_name='Статус заказа')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Создан')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.periodofstorage', verbose_name='Период хранение')),
                ('quantity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.quantityoftires', verbose_name='Количество')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.tiresize', verbose_name='Размер шин')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
