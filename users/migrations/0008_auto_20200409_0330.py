# Generated by Django 3.0.3 on 2020-04-08 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200409_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='full.jpg', upload_to=''),
        ),
    ]
