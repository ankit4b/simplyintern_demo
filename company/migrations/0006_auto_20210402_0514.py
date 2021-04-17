# Generated by Django 3.1.7 on 2021-04-01 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20210402_0455'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mob',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='company/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook_link',
            field=models.URLField(default='#', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github_link',
            field=models.URLField(default='#', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter_link',
            field=models.URLField(default='#', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='youtube_link',
            field=models.URLField(default='#', null=True),
        ),
    ]
