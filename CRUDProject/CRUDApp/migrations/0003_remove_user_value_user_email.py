# Generated by Django 4.2.5 on 2023-09-12 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUDApp', '0002_rename_val_user_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='value',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
