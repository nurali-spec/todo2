# Generated by Django 3.2.4 on 2021-08-23 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('is_closed', models.BooleanField(verbose_name=False)),
                ('is_favorite', models.BooleanField(verbose_name=False)),
            ],
        ),
    ]
