# Generated by Django 3.2.2 on 2021-06-01 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20210601_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='result_quizz',
            name='quizz',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='quizz', to='website.quizz'),
        ),
    ]
