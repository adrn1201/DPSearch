# Generated by Django 4.0.3 on 2023-01-09 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_options_alter_tag_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
