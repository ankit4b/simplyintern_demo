# Generated by Django 3.1.7 on 2021-04-01 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20210331_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='interns_hired',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='internship_post',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='no_of_employees',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
