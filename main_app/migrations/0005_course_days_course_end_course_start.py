# Generated by Django 5.1.1 on 2024-09-24 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_enrollment'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='days',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='start',
            field=models.DateTimeField(null=True),
        ),
    ]
