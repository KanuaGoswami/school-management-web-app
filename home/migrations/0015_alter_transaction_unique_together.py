# Generated by Django 4.1.3 on 2023-01-09 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_transaction_id_alter_transaction_student'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='transaction',
            unique_together={('student', 'amount')},
        ),
    ]
