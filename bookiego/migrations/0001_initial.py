# Generated by Django 2.2 on 2020-05-31 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=90)),
                ('last_name', models.CharField(max_length=90)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.TextField()),
                ('address', models.TextField()),
                ('package_name', models.TextField()),
            ],
        ),
    ]