# Generated by Django 3.2.5 on 2021-08-19 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icon', '0015_likedcomment_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likedcomment',
            name='choice',
            field=models.CharField(default='No', max_length=50),
        ),
    ]