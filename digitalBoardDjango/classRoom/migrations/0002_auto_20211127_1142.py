# Generated by Django 3.2.5 on 2021-11-27 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classRoom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitassignment',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='submitassignment',
            name='comment',
            field=models.TextField(blank=True, default='None'),
        ),
    ]