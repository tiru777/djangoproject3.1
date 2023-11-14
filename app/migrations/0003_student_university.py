# Generated by Django 4.2.7 on 2023-11-09 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_topping_pizza'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('dob', models.DateField(blank=True, null=True)),
                ('age', models.IntegerField()),
                ('photo', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=200)),
                ('dp_id', models.IntegerField()),
                ('dp_info', models.TextField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
    ]
