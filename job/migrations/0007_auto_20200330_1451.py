# Generated by Django 2.2.10 on 2020-03-30 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_auto_20200329_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='sub_no',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
