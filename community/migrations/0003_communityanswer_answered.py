# Generated by Django 2.2.4 on 2019-08-24 14:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20190824_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityanswer',
            name='answered',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]