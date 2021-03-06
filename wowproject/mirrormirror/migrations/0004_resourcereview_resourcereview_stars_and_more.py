# Generated by Django 4.0.3 on 2022-05-27 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mirrormirror', '0003_websitereview'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcereview',
            name='resourcereview_stars',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default='1'),
        ),
        migrations.AlterField(
            model_name='resourcereview',
            name='resourcereview_comment',
            field=models.TextField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='resourcereview',
            name='resourcereview_username',
            field=models.CharField(max_length=4000),
        ),
    ]
