# Generated by Django 4.2.5 on 2023-09-25 14:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "adminapp",
            "0009_course_ltps_course_credits_alter_course_academicyear_and_more",
        ),
    ]

    operations = [
        migrations.DeleteModel(
            name="FacultyCourseMappings",
        ),
    ]