# Generated by Django 2.1.7 on 2019-03-03 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('Course', models.CharField(max_length=100)),
                ('Class', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            model_name  = 'Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class', models.CharField(max_length=100)),
            ],
        ),
    ]
