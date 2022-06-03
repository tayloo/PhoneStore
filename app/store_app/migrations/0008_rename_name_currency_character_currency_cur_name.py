# Generated by Django 4.0.4 on 2022-06-03 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0007_rename_picture_product_picture1_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currency',
            old_name='name',
            new_name='character',
        ),
        migrations.AddField(
            model_name='currency',
            name='cur_name',
            field=models.CharField(default='USD', max_length=3),
        ),
    ]
