# Generated by Django 4.0.4 on 2022-05-22 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0020_alter_vacation_vacend_alter_vacation_vacstart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=7),
        ),
        migrations.AlterField(
            model_name='employee',
            name='maritalstatus',
            field=models.CharField(choices=[('S', 'Single'), ('M', 'Married')], max_length=9),
        ),
    ]
