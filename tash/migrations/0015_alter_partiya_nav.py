# Generated by Django 4.1.7 on 2023-02-25 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tash', '0014_alter_partiya_bunt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partiya',
            name='nav',
            field=models.CharField(help_text='Анд-35,Анд-36,Шарк', max_length=30, null=True, verbose_name='Селекцион Нав'),
        ),
    ]
