# Generated by Django 3.1.7 on 2021-04-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20210426_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='certificate_file',
            field=models.FileField(blank=True, null=True, upload_to='student/certificate/'),
        ),
    ]
