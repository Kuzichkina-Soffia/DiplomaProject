# Generated by Django 4.2.10 on 2024-02-08 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StandartUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=256)),
                ('username', models.CharField(max_length=150, verbose_name='username')),
                ('last_name', models.CharField(max_length=150)),
                ('date_joined', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=150)),
            ],
        ),
    ]
