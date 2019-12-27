# Generated by Django 3.0.1 on 2019-12-27 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20191227_0324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='damage',
            new_name='damage1',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='heal',
            new_name='damage2',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='score',
            new_name='heal1',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='killed_alias',
            new_name='killed1',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='killed_hostiles',
            new_name='killed2',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='spawned_alias',
            new_name='spawned1',
        ),
        migrations.AddField(
            model_name='match',
            name='heal2',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='score1',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='score2',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='spawned2',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
