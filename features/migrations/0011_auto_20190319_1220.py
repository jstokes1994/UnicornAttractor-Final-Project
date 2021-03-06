# Generated by Django 2.0 on 2019-03-19 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0010_auto_20190319_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='num_vote_down',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='feature',
            name='num_vote_up',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='feature',
            name='vote_score',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
