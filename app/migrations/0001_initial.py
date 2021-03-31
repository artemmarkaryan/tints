# Generated by Django 3.1.7 on 2021-03-31 16:30

from django.db import migrations, models
import django.db.models.deletion
import helpers.images


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('translitName', models.CharField(max_length=255, verbose_name='Транслит')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='ModelWithImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=511, verbose_name='Название')),
                ('translit_name', models.CharField(max_length=511, verbose_name='Транслит')),
                ('description', models.TextField(verbose_name='Описание')),
                ('new', models.BooleanField(default=False)),
                ('top', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Shade',
            fields=[
                ('modelwithimage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.modelwithimage')),
                ('name', models.CharField(max_length=512, verbose_name='Название')),
                ('image', models.FileField(blank=True, null=True, upload_to=helpers.images.create_image_path, verbose_name='Фото')),
                ('image_url', models.CharField(blank=True, max_length=1023, null=True, verbose_name='Ссылка на фото')),
            ],
            bases=('app.modelwithimage',),
        ),
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Название')),
                ('translitName', models.CharField(blank=True, max_length=512, null=True, verbose_name='Транслит')),
                ('vendorCode', models.CharField(max_length=512, unique=True, verbose_name='Название')),
                ('oldPrice', models.FloatField(blank=True, null=True, verbose_name='Старая цена')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('weight', models.IntegerField(verbose_name='Объём (мл)')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product', verbose_name='Продукт')),
            ],
        ),
        migrations.CreateModel(
            name='SkuImage',
            fields=[
                ('modelwithimage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.modelwithimage')),
                ('image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл изображения')),
                ('image_url', models.CharField(max_length=1023, verbose_name='Ссылка яна изображение')),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sku', verbose_name='SKU')),
            ],
            bases=('app.modelwithimage',),
        ),
        migrations.AddField(
            model_name='product',
            name='shade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='app.shade', verbose_name='Оттенок'),
        ),
    ]