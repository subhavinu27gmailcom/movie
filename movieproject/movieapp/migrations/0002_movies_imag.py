# Generated by Django 5.0 on 2023-12-08 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='imag',
            field=models.ImageField(default='name', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
