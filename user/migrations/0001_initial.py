# Generated by Django 3.0.4 on 2020-03-29 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('school_id', models.CharField(max_length=32, unique=True)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=6)),
                ('type', models.CharField(choices=[('admin', 'Administrator'), ('student', 'Student'), ('teacher', 'Teacher')], default='student', max_length=7)),
                ('avatar', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=32, null=True)),
                ('real_name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('note', models.CharField(max_length=140, null=True)),
                ('status', models.CharField(choices=[('appending', 'Appending'), ('active', 'Active'), ('declined', 'Declined'), ('deleted', 'Deleted')], default='active', max_length=9)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'school_users',
            },
        ),
    ]
