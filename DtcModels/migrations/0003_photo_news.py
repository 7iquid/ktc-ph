# Generated by Django 4.0 on 2022-08-24 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DtcModels', '0002_remove_newsfeeds_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='news',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DtcModels.newsfeeds'),
        ),
    ]
