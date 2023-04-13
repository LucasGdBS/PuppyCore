from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_puppy_core', '0007_alter_pet_tutor'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartaoVacina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoVacina', models.CharField(max_length=30)),
                ('dataVacina', models.DateField(blank=True, null=True)),
                ('pet', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_puppy_core.pet')),
            ],
        ),
    ]
