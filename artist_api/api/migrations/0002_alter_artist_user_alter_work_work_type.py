# Generated by Django 4.2.7 on 2023-12-02 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='work',
            name='work_type',
            field=models.CharField(choices=[('YT', 'Youtube'), ('IG', 'Instagram'), ('OT', 'Other')], max_length=2, null=True),
        ),
    ]
