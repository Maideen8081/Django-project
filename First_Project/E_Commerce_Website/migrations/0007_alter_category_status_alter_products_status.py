# Generated by Django 5.1.3 on 2024-11-14 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Commerce_Website', '0006_category_trending_alter_category_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=False, help_text='0-show,1-Hidden'),
        ),
        migrations.AlterField(
            model_name='products',
            name='status',
            field=models.BooleanField(default=False, help_text='0-show,1-Hidden'),
        ),
    ]