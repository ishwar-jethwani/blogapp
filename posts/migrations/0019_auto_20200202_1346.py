# Generated by Django 2.2 on 2020-02-02 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_auto_20200130_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(upload_to='s3://wordblogger/media/'),
        ),
    ]