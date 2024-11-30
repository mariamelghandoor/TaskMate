# Generated by Django 5.0.9 on 2024-11-29 11:09

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('environment', '0001_initial'),
        ('users', '0003_alter_login_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed')], default='PENDING', max_length=20)),
                ('start_date', models.DateTimeField(default=datetime.date.today)),
                ('deadline', models.DateTimeField()),
                ('priority', models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], default='MEDIUM', max_length=20)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_tasks', to='users.login')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_tasks', to='users.login')),
                ('environment_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='environment.environment')),
                ('table', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='environment.table')),
            ],
        ),
    ]
    class Meta:
        ordering = ['priority', 'deadline'] 

