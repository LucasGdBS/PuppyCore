# Generated by Django 4.2 on 2023-05-12 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_puppy_core', '0013_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='dtNasc',
            field=models.DateField(blank=True, default=0, null=True),
        ),
    ]
