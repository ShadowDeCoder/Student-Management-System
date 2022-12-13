# Generated by Django 4.1.3 on 2022-12-06 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.CharField(max_length=100)),
                ('std_name', models.CharField(max_length=200)),
                ('std_email', models.EmailField(max_length=254)),
                ('std_number', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
