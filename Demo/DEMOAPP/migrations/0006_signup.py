# Generated by Django 3.1.7 on 2021-05-10 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DEMOAPP', '0005_auto_20210507_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('an', models.CharField(max_length=16, unique=True)),
                ('mn', models.CharField(max_length=11)),
                ('cid', models.CharField(max_length=9)),
                ('cpass', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'signup3',
            },
        ),
    ]
