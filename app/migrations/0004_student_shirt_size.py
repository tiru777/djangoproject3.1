# Generated by Django 4.2.7 on 2023-11-09 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_student_university'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='shirt_size',
            field=models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1, null=True),
        ),
    ]
