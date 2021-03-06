# Generated by Django 3.1.7 on 2021-03-19 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('isCompany', models.BooleanField(default=True)),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('place', models.CharField(max_length=128)),
                ('duration', models.CharField(max_length=128)),
                ('stipend', models.CharField(max_length=128)),
                ('no_of_openings', models.IntegerField()),
                ('perks', models.CharField(max_length=128)),
                ('skills', models.CharField(max_length=128)),
                ('about_internship', models.TextField()),
                ('who_can_apply', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
            options={
                'verbose_name': 'Internship',
                'verbose_name_plural': 'Internships',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
