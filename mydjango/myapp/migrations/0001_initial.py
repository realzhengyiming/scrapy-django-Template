# Generated by Django 2.0 on 2019-12-17 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classify_name', models.CharField(max_length=191, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meiju',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191)),
                ('url', models.CharField(max_length=191, unique=True)),
                ('grade', models.CharField(default='', max_length=191)),
                ('imgurl', models.CharField(default='', max_length=191)),
                ('classification', models.ManyToManyField(to='myapp.Classification')),
            ],
        ),
    ]
