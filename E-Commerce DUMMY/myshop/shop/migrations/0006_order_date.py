# Generated by Django 2.2.5 on 2020-11-08 04:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20201108_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]