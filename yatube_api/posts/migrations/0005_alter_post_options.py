# Generated by Django 3.2.16 on 2023-06-18 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_follow_unique_user_following'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pub_date',)},
        ),
    ]
