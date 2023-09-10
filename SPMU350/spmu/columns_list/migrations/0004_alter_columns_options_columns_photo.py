# Generated by Django 4.1.3 on 2022-12-07 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('columns_list', '0003_alter_columns_info_alter_columns_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='columns',
            options={'ordering': ['title'], 'verbose_name': 'Выпускник', 'verbose_name_plural': 'Выпускники'},
        ),
        migrations.AddField(
            model_name='columns',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]