# Generated by Django 4.2.4 on 2023-08-13 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('content', models.TextField(verbose_name='контент')),
                ('cover', models.ImageField(upload_to='covers', verbose_name='обложка')),
                ('views_count', models.TextField(verbose_name='количество просмотров')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]