# Generated by Django 3.2 on 2023-03-19 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='nickname',
            field=models.CharField(default='pemi', max_length=10),
            preserve_default=False,
        ),
    ]