# Generated by Django 4.2 on 2023-04-28 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_puppy_core', '0012_alter_pet_tutor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
    ]
