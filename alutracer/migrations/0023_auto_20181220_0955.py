# Generated by Django 2.1.3 on 2018-12-20 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alutracer', '0022_auto_20181220_0951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='user',
        ),
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
