# Generated by Django 4.2.4 on 2024-04-05 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("masterdata", "0004_returnreason"),
        ("product", "0008_remove_variant_attributes_variantattributes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="variantattributes",
            name="attributes",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="attributes",
                to="masterdata.attribute",
                verbose_name="Attributes",
            ),
        ),
        migrations.AlterField(
            model_name="variantattributes",
            name="variant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="variant",
                to="product.variant",
                verbose_name="Variant",
            ),
        ),
    ]
