# Generated by Django 5.0.9 on 2024-12-21 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('environment_id', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=255, unique=True)),
                ('is_private', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'environment',
            },
        ),
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('search_history_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'search_history',
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('table_id', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'table',
            },
        ),
        migrations.CreateModel(
            name='UserCanAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_accessibility', models.CharField(choices=[('Participant', 'Participant'), ('subadmin', 'subadmin'), ('Admin', 'Admin')], max_length=20)),
                ('invitation_status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
            ],
            options={
                'db_table': 'user_can_access',
            },
        ),
    ]
