# Generated by Django 2.1.4 on 2019-01-07 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbv_app', '0002_auto_20190107_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]