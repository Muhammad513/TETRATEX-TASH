# Generated by Django 4.1.7 on 2023-02-23 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(blank=True, default='default/default.jpg', null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pic_thumbnail',
            field=models.ImageField(blank=True, default='default/thumbnail.jpg', null=True, upload_to='img'),
        ),
    ]
