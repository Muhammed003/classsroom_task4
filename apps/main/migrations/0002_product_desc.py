# Generated by Django 3.2 on 2022-05-26 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
