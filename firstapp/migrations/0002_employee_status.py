# Generated by Django 3.1.1 on 2020-09-12 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]