# Generated by Django 4.1.2 on 2022-10-17 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_text',
            field=models.CharField(max_length=10000),
        ),
    ]
