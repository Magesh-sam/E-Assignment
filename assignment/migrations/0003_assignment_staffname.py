# Generated by Django 3.0.7 on 2020-12-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_assignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='staffname',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
