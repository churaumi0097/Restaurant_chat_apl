# Generated by Django 4.2.16 on 2024-11-14 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_difymodel_delete_textgeneration"),
    ]

    operations = [
        migrations.RenameField(
            model_name="difymodel",
            old_name="input",
            new_name="query",
        ),
    ]