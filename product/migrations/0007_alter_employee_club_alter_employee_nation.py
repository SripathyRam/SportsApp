# Generated by Django 4.1.1 on 2022-10-20 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_employee_club_alter_employee_nation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='club',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='nation',
            field=models.CharField(max_length=100),
        ),
    ]
