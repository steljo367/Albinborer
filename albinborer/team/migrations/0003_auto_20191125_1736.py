# Generated by Django 2.2.7 on 2019-11-25 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20191125_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('email_url', models.URLField(unique=True)),
                ('tele_phone', models.CharField(max_length=264, unique=True)),
                ('tele_fax', models.CharField(max_length=264, unique=True)),
                ('headshot', models.ImageField(blank=True, null=True, upload_to='Member_profile_upload/')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Designation')),
            ],
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.AlterField(
            model_name='accessrecord',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Member'),
        ),
        migrations.DeleteModel(
            name='Website',
        ),
    ]
