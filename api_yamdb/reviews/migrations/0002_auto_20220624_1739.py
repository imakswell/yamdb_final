# Generated by Django 2.2.16 on 2022-06-24 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '__first__'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='title_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titles_review', to='titles.Title', verbose_name='Произведение'),
        ),
        migrations.DeleteModel(
            name='Title',
        ),
    ]
