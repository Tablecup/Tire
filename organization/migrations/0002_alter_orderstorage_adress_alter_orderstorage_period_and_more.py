# Generated by Django 4.0.5 on 2023-04-09 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstorage',
            name='adress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.adresssirvice', verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='orderstorage',
            name='period',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.periodofstorage', verbose_name='Период'),
        ),
        migrations.AlterField(
            model_name='orderstorage',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.tiresize', verbose_name='Размер'),
        ),
    ]