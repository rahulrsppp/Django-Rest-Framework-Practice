# Generated by Django 2.1.4 on 2019-02-16 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(default='', max_length=254)),
                ('mobile', models.IntegerField(default='')),
                ('username', models.CharField(default='', max_length=20)),
                ('password', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(default='', max_length=254)),
                ('mobile', models.IntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='VoterList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(default='', max_length=254)),
                ('mobile', models.IntegerField(default='')),
                ('city', models.CharField(default='', max_length=20)),
                ('type', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
