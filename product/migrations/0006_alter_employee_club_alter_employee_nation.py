# Generated by Django 4.1.1 on 2022-10-20 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_employee_defending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='nation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.role'),
        ),
    ]
