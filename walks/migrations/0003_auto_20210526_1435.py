# Generated by Django 3.2.3 on 2021-05-26 14:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('walks', '0002_alter_stop_location_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stop',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='walk',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stop',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='walk',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
