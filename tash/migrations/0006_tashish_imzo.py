# Generated by Django 4.1.7 on 2023-02-23 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tash', '0005_remove_partiya_xosil'),
    ]

    operations = [
        migrations.AddField(
            model_name='tashish',
            name='imzo',
            field=models.BooleanField(default=False),
        ),
    ]
