# Generated by Django 2.1.1 on 2018-09-06 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20180906_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentreport',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='dashboard.Student'),
        ),
    ]
