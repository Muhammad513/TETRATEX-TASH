# Generated by Django 4.1.7 on 2023-02-25 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tash', '0011_paxtanavi'),
    ]

    operations = [
        migrations.AddField(
            model_name='partiya',
            name='seleksiya',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tash.paxtanavi'),
        ),
    ]
