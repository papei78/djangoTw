# Generated by Django 5.0.4 on 2024-04-27 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='additional_info',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='book_count',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='books',
            field=models.ManyToManyField(blank=True, help_text='book that are currently rented', to='books.book'),
        ),
        migrations.AddField(
            model_name='customer',
            name='rating',
            field=models.PositiveSmallIntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
