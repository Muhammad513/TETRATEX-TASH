# Generated by Django 4.1.7 on 2023-02-22 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tash', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partiya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xosil', models.CharField(max_length=4)),
                ('partiya', models.CharField(max_length=7)),
                ('bunt', models.CharField(max_length=20)),
                ('nav', models.CharField(max_length=30)),
                ('sort', models.CharField(max_length=1)),
                ('snif', models.CharField(max_length=1)),
                ('sofVazn', models.FloatField()),
                ('xisobiy', models.FloatField()),
                ('kond', models.FloatField()),
                ('ifloslik', models.FloatField()),
                ('namlik', models.FloatField()),
            ],
        ),
    ]
