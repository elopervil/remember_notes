# Generated by Django 4.1.2 on 2022-11-21 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('panelNotes', '0004_alter_notes_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='owner_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
