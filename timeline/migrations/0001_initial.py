# Generated by Django 2.0.6 on 2018-06-04 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('status', models.TextField()),
                ('like', models.IntegerField()),
            ],
        ),
    ]
