# Generated by Django 2.2.7 on 2019-11-25 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_auto_20191125_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='location',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='tele_fax',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='tele_phone',
            field=models.CharField(max_length=12, null=True),
        ),
    ]