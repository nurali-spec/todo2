# Generated by Django 3.2.4 on 2021-08-23 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
