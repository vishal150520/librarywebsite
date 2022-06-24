# Generated by Django 3.2.9 on 2022-06-23 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admindetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('dateofbirth', models.EmailField(max_length=50, unique=True)),
                ('email', models.CharField(max_length=50)),
                ('contactno', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
