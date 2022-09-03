# Generated by Django 4.1 on 2022-09-03 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0003_remove_size_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(choices=[('Sm', 'Small'), ('Md', 'Medium'), ('Lg', 'Large')], default='Md', max_length=10, verbose_name='Size'),
        ),
    ]
