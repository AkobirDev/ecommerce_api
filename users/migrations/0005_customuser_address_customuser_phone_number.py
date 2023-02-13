# Generated by Django 4.1.6 on 2023-02-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
