# Generated by Django 4.2 on 2023-05-13 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_puppy_core', '0014_alter_pet_dtnasc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartaovacina',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_puppy_core.pet'),
        ),
    ]
