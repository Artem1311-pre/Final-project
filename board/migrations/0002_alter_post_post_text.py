# Generated by Django 4.1.7 on 2023-07-01 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(),
        ),
    ]