# Generated by Django 5.0.7 on 2024-07-23 04:50

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_number', models.CharField(default='000-00000', max_length=10, unique=True, verbose_name='Номер материала')),
                ('title', models.CharField(max_length=100, verbose_name='Mатериал')),
                ('text', models.TextField(verbose_name='Oписание материала')),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Скидка действительна до')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Старая цена')),
                ('img_content', models.ImageField(default='default_content.png', upload_to='content_images', verbose_name='Фото товара')),
                ('avtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
