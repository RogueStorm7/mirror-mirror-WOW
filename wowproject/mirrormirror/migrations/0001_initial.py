# Generated by Django 4.0.3 on 2022-05-24 00:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('commentor_name', models.CharField(default='Anonymous', help_text='  ', max_length=255)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, help_text='Date & Time Stamp')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=False, max_length=100)),
                ('description', models.CharField(default=True, max_length=100)),
                ('resource_name', models.CharField(default=False, max_length=150)),
                ('resource_address', models.CharField(default=False, max_length=150)),
                ('resource_city', models.CharField(default=False, max_length=150)),
                ('resource_state', models.CharField(default=False, max_length=20)),
                ('resource_zip', models.CharField(default=False, max_length=10)),
                ('resource_phone', models.CharField(default=False, max_length=150)),
                ('resource_url', models.URLField(default=True, max_length=150)),
                ('resource_date', models.DateTimeField(auto_now_add=True)),
                ('category_tags', models.ManyToManyField(to='mirrormirror.category')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourcereview_username', models.TextField(max_length=4000)),
                ('resourcereview_comment', models.TextField(max_length=4000)),
                ('resourcereview_date', models.DateTimeField(auto_now_add=True)),
                ('resourcereview_stars', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mirrormirror.resource')),
            ],
        ),
    ]
