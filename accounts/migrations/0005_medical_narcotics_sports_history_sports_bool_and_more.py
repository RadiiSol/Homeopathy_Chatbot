# Generated by Django 4.1.1 on 2022-09-14 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_patient_medical_history_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medical_narcotics_sports_history',
            name='sports_bool',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medical_narcotics_sports_history',
            name='sports_name',
            field=models.CharField(default='NA', max_length=40),
        ),
        migrations.AlterField(
            model_name='patient_medical_history',
            name='sex',
            field=models.CharField(max_length=6),
        ),
    ]
