# Generated by Django 5.1.2 on 2025-01-26 13:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_alter_article_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="featured_image",
            field=models.ImageField(
                default="featured_images/default_image.jpg",
                upload_to="featured_images/",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        ["png", "jpg", "jpeg", "gif"]
                    )
                ],
            ),
        ),
    ]
