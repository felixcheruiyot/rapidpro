# Generated by Django 2.0.8 on 2018-08-29 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("flows", "0174_populate_flow_is_system")]

    operations = [
        migrations.AlterField(
            model_name="flow",
            name="flow_type",
            field=models.CharField(
                choices=[("M", "Message flow"), ("V", "Phone call flow"), ("S", "Surveyor flow"), ("U", "USSD flow")],
                default="M",
                help_text="The type of this flow",
                max_length=1,
            ),
        )
    ]
