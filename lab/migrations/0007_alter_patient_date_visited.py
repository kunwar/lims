# Generated by Django 4.1.7 on 2023-03-14 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0006_alter_completebloodcount_basophils_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_visited',
            field=models.DateField(),
        ),
    ]