# Generated by Django 3.1.3 on 2021-03-27 20:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_person_date_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='bio',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='person',
            name='age',
        ),
        migrations.RemoveField(
            model_name='person',
            name='salary',
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default=datetime.datetime(2021, 3, 27, 20, 34, 13, 55514, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.CharField(default=datetime.datetime(2021, 3, 27, 20, 34, 28, 616068, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]
