# Generated by Django 2.2.4 on 2019-08-25 01:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_expert_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmercropyield',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]