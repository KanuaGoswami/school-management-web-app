# Generated by Django 4.1.3 on 2023-01-09 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_student_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contact',
            unique_together={('name', 'email', 'subject', 'message')},
        ),
        migrations.AlterUniqueTogether(
            name='gallery',
            unique_together={('title', 'desc')},
        ),
        migrations.AlterUniqueTogether(
            name='result',
            unique_together={('student', 'examname', 'english', 'math', 'science', 'sst', 'hindi')},
        ),
        migrations.AlterUniqueTogether(
            name='teacher',
            unique_together={('name', 'address', 'mobile', 'dob', 'designation', 'desc', 'gender', 'qualification')},
        ),
    ]
