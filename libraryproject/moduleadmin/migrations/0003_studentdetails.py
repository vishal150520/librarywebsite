# Generated by Django 3.2.9 on 2022-06-23 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduleadmin', '0002_bookdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentfname', models.CharField(max_length=50)),
                ('studentlname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('rollno', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
            ],
        ),
    ]
