# Generated by Django 4.2.4 on 2024-04-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_remove_collection_collections_collectionitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='is_in_home_page',
            field=models.BooleanField(default=False, verbose_name='Display In Home Page'),
        ),
        migrations.AddField(
            model_name='lookbook',
            name='is_in_home_page',
            field=models.BooleanField(default=False, verbose_name='Display In Home Page'),
        ),
    ]
