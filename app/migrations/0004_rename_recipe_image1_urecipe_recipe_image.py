# Generated by Django 4.1 on 2022-09-16 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_urecipe_recipe_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urecipe',
            old_name='recipe_image1',
            new_name='recipe_image',
        ),
    ]
