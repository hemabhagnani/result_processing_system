# Generated by Django 2.2.10 on 2020-03-29 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_remove_student_student_dept_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_dept_no',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='job.department'),
            preserve_default=False,
        ),
    ]