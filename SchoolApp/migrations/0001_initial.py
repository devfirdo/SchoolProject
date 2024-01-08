# Generated by Django 5.0 on 2024-01-03 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
                ('course_fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255)),
                ('student_age', models.IntegerField()),
                ('student_email', models.EmailField(max_length=254)),
                ('student_joining_date', models.DateField()),
                ('student_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.course')),
            ],
        ),
    ]
