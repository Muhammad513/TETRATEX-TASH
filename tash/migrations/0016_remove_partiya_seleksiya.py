# Generated by Django 4.1.7 on 2023-02-25 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tash', '0015_alter_partiya_nav'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partiya',
            name='seleksiya',
        ),
    ]
