# Generated by Django 4.0.5 on 2022-07-13 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_alter_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.URLField(default='https://t4.ftcdn.net/jpg/02/66/60/17/360_F_266601726_NCXy2AIRecYluwp5BUKOXQAWo35Seilr.jpg'),
        ),
    ]
