# Generated by Django 3.1.2 on 2020-11-12 01:29

import ayen_task.core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='uploads', validators=[ayen_task.core.models.validate_file_extension])),
            ],
        ),
    ]
