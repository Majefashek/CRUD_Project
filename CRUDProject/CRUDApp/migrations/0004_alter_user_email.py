# Generated by Django 4.2.5 on 2023-09-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUDApp', '0003_remove_user_value_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
