# Generated by Django 4.0.6 on 2022-11-05 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contrat', '0002_alter_contrat_sales_contact'),
        ('événement', '0003_alter_event_support_contact'),
        ('authentification', '0002_user_alter_client_sales_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]