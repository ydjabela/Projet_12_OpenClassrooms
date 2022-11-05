# Generated by Django 4.1.2 on 2022-11-04 16:44

import authentification.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('role', models.CharField(blank=True, choices=[('sales_member', 'sales_member'), ('management_member', 'management_member'), ('support_member', 'support_member')], max_length=20, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', authentification.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='sales_contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentification.user'),
        ),
    ]