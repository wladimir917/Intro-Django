# Generated by Django 2.1 on 2018-08-27 22:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('sprint_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sprint_name', models.CharField(max_length=40)),
                ('sprint_status', models.CharField(max_length=20)),
                ('submission_self_rating', models.PositiveSmallIntegerField()),
                ('what_went_well', models.TextField(blank=True)),
                ('what_could_have_gone_better', models.TextField(blank=True)),
                ('requested_improvements', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentReport',
            fields=[
                ('student_report_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('current_section', models.CharField(max_length=10)),
                ('project_manager', models.CharField(max_length=30)),
                ('submitted_sprints', models.PositiveSmallIntegerField()),
                ('passed_sprints', models.PositiveSmallIntegerField()),
                ('sprint_pass_rate', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='sprint',
            name='student_report_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.StudentReport'),
        ),
    ]