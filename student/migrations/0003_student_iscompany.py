# Generated by Django 3.1.7 on 2021-03-30 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210319_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='isCompany',
            field=models.BooleanField(default=False),
        ),
    ]
