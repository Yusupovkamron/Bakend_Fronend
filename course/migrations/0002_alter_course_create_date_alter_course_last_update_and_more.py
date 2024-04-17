# Generated by Django 5.0.4 on 2024-04-16 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='create_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='last_update',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='create_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='last_update',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='create_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='last_update',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='create_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_update',
            field=models.DateField(auto_now=True),
        ),
    ]
