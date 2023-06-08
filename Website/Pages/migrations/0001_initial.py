# Generated by Django 4.0.4 on 2022-05-19 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100, unique=True)),
                ('phoneNum', models.CharField(max_length=15)),
                ('dateofBirth', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6)),
                ('maritalstatus', models.CharField(choices=[('S', 'Single'), ('M', 'Married')], max_length=7)),
                ('availablevac', models.IntegerField()),
                ('approvedvac', models.IntegerField()),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
