# Generated by Django 4.2 on 2024-12-17 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_contact_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='lastName',
            new_name='last_name',
        ),
    ]
