# Generated by Django 3.2 on 2022-08-21 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('cuerpo', models.TextField()),
                ('fecha', models.DateField()),
                ('imagen', models.ImageField(null=True, upload_to='actividades')),
            ],
        ),
    ]
