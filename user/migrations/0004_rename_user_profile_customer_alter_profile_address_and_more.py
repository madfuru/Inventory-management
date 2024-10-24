# Generated by Django 5.1.1 on 2024-10-09 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_customer_profile_user_alter_profile_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='customer',
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(default='Unknown', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='unknown', max_length=50),
            preserve_default=False,
        ),
    ]
