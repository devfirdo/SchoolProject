# Generated by Django 5.0 on 2024-01-04 08:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_age', models.IntegerField()),
                ('teacher_address', models.CharField(max_length=255)),
                ('teacher_number', models.IntegerField()),
                ('teacher_image', models.ImageField(blank=True, upload_to='image/')),
                ('teacher_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.course')),
                ('teacher_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
