# Generated by Django 3.1.6 on 2021-03-08 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0038_auto_20210224_1939'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='answer',
            name='points',
            field=models.CharField(choices=[('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10)], default=0, max_length=2),
        ),
    ]
