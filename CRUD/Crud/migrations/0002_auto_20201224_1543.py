# Generated by Django 3.1.4 on 2020-12-24 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(help_text='What do you think ?'),
        ),
    ]
