# Generated by Django 3.1.4 on 2021-01-08 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_solved_quizzes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='solved_quizzes',
        ),
    ]
