# Generated by Django 4.1.7 on 2023-02-23 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tash', '0006_tashish_imzo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tashish',
            name='ptm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tash.punkt'),
        ),
    ]
