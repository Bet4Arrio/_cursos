# Generated by Django 3.2 on 2021-04-30 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20210430_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeworksubmission',
            name='submission_description',
            field=models.TextField(max_length=200, null=True),
        ),
    ]