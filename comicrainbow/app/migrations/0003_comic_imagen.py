# Generated by Django 3.1.2 on 2020-12-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_contacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
