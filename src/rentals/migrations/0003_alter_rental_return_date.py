# Generated by Django 5.0.4 on 2024-04-27 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0002_alter_rental_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='return_date',
            field=models.DateField(blank=True, help_text='actual return date', null=True),
        ),
    ]
