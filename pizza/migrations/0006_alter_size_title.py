# Generated by Django 4.1 on 2022-09-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0005_size_title_alter_size_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]