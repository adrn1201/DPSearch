# Generated by Django 4.0.3 on 2023-01-16 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title'], 'verbose_name_plural': 'Projects'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name_plural': 'Reviews'},
        ),
    ]
