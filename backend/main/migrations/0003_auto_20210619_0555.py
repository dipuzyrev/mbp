# Generated by Django 3.2.4 on 2021-06-19 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210619_0527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tonometer',
            name='user',
        ),
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='weight',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
