# Generated by Django 4.1 on 2022-09-03 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='size',
            field=models.CharField(choices=[('Sm', 'Small'), ('Md', 'Medium'), ('Lg', 'Large')], default='Md', max_length=10),
        ),
    ]