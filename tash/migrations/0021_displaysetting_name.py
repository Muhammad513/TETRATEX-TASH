# Generated by Django 4.1.7 on 2023-02-25 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tash', '0020_displaysetting'),
    ]

    operations = [
        migrations.AddField(
            model_name='displaysetting',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
