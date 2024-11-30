# Generated by Django 5.0.9 on 2024-11-29 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_login_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='login',
            name='badge_name',
            field=models.CharField(default='HardWorker', max_length=255),
        ),
        migrations.AddField(
            model_name='login',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='login',
            name='phone_num',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='login',
            name='theme_is_light',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterModelTable(
            name='login',
            table='users',
        ),
    ]
