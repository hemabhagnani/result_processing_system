# Generated by Django 2.2.10 on 2020-03-30 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_auto_20200330_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='sub_no',
            field=models.TextField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
