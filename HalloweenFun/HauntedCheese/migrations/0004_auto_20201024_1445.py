# Generated by Django 3.1.2 on 2020-10-24 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HauntedCheese', '0003_auto_20201024_1237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='list_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='list_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='list_iterator',
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='HauntedCheese.userprofile'),
        ),
        migrations.DeleteModel(
            name='TodoIterator',
        ),
    ]
