# Generated by Django 2.2.3 on 2020-05-16 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200515_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='coverimage/%Y/%m/%d/', verbose_name='封面图片'),
        ),
    ]
