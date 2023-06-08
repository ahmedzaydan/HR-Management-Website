# Generated by Django 4.0.4 on 2022-05-19 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0015_rename_idr_employee_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='importantMeetings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('declared', models.IntegerField(default=0)),
                ('planned', models.IntegerField(default=0)),
                ('taken', models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='OfficialHolidays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.IntegerField(default=3)),
                ('taken', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Trainings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.IntegerField(default=3)),
                ('taken', models.IntegerField(default=3)),
            ],
        ),
    ]