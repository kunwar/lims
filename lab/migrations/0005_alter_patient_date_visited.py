# Generated by Django 4.1.7 on 2023-03-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_alter_completebloodcount_hct_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_visited',
            field=models.DateTimeField(),
        ),
    ]
