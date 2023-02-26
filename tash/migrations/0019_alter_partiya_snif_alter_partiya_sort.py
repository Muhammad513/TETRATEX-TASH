# Generated by Django 4.1.7 on 2023-02-25 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tash', '0018_alter_paxtanavi_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partiya',
            name='snif',
            field=models.CharField(choices=[('1', '1-Сниф'), ('2', '2-Сниф'), ('3', '3-Сниф')], max_length=1, verbose_name='Пахтанинг снифи'),
        ),
        migrations.AlterField(
            model_name='partiya',
            name='sort',
            field=models.CharField(choices=[('1', '1-Сoрт'), ('2', '2-Сoрт'), ('3', '3-Сoрт'), ('4', '4-Сoрт'), ('5', '5-Сoрт')], max_length=1, verbose_name='Пахтанинг Сорти'),
        ),
    ]