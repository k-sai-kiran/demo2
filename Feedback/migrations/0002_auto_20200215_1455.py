# Generated by Django 2.2.2 on 2020-02-15 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='AreaofIssue',
            field=models.CharField(blank=True, default=None, max_length=40, null=True),
        ),
    ]