# Generated by Django 2.1.3 on 2019-02-05 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alutracer', '0038_auto_20190205_0036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalinformation',
            old_name='teaching_Learning',
            new_name='teaching_learning',
        ),
    ]
