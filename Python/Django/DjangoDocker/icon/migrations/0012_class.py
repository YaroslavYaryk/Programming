# Generated by Django 3.2.5 on 2021-08-18 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icon', '0011_likedcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_comment', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]
