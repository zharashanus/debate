# Generated by Django 5.0.4 on 2024-04-18 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicuser',
            name='role',
            field=models.CharField(blank=True, choices=[('Линкольн', 'Линкольн'), ('Дуглас', 'Дуглас'), ('Lincoln', 'Lincoln'), ('Duoglas', 'Duoglas')], max_length=255, null=True),
        ),
    ]
