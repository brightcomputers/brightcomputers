# Generated by Django 3.0.3 on 2020-04-08 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200406_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/static/full.jpg', upload_to=''),
        ),
    ]
