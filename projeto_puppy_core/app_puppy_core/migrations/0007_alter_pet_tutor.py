# Generated by Django 4.2 on 2023-04-11 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_puppy_core', '0006_pet_tutor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='tutor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_puppy_core.tutor'),
        ),
    ]
