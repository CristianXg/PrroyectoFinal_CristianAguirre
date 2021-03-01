# Generated by Django 3.1.4 on 2021-03-01 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_category', models.IntegerField(default=0)),
                ('name', models.CharField(default=0, max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('category', models.IntegerField(blank=True, default=0)),
                ('title', models.CharField(default=0, max_length=400)),
                ('text', models.CharField(default=0, max_length=400)),
                ('author', models.IntegerField(default=0)),
            ],
        ),
    ]
