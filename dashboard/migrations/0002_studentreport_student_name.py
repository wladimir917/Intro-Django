# Generated by Django 2.1 on 2018-08-27 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentreport',
            name='student_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]