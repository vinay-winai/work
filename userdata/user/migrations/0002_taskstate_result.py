# Generated by Django 4.1.7 on 2023-02-27 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskstate',
            name='result',
            field=models.CharField(default='none', max_length=10),
        ),
    ]