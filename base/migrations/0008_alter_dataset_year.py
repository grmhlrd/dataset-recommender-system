# Generated by Django 4.2.5 on 2023-11-29 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_dataset_archived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='year',
            field=models.DateField(blank=True),
        ),
    ]
