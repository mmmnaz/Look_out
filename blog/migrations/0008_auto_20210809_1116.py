# Generated by Django 3.1.7 on 2021-08-09 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210809_0047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='description',
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
