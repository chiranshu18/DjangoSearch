# Generated by Django 4.2.2 on 2023-06-17 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('serial_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=42)),
                ('number', models.TextField()),
            ],
        ),
    ]
