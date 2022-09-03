# Generated by Django 4.1 on 2022-09-03 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0004_alter_size_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='title',
            field=models.CharField(default='title', max_length=100),
        ),
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(choices=[('Sm', 'Small'), ('Md', 'Medium'), ('Lg', 'Large')], max_length=10),
        ),
    ]