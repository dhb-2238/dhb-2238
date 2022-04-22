# Generated by Django 2.2 on 2021-12-15 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='departments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Serial_number', models.CharField(max_length=50)),
                ('boss', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=40)),
                ('place', models.CharField(max_length=60)),
                ('category', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ids', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=15)),
                ('service', models.CharField(max_length=20)),
                ('national', models.CharField(max_length=10)),
                ('Native_place', models.CharField(max_length=20)),
                ('birthday', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=40)),
                ('edom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.departments')),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='useremployees',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('passwd', models.CharField(max_length=20, verbose_name='密码')),
                ('san', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.employees')),
            ],
            options={
                'db_table': 'useremployees',
            },
        ),
    ]
