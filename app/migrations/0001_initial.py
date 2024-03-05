# Generated by Django 5.0.3 on 2024-03-05 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('work_place', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('gender', models.CharField(choices=[('F', 'Женский'), ('M', 'Мужской')], max_length=1)),
            ],
        ),
    ]
