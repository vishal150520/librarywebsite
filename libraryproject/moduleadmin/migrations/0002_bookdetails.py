# Generated by Django 3.2.9 on 2022-06-23 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduleadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=50)),
                ('writerName', models.CharField(max_length=50)),
                ('edition', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('catogory', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
            ],
        ),
    ]