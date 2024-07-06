# Generated by Django 5.0.6 on 2024-06-28 02:39

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("App01", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="board",
            name="down",
        ),
        migrations.RemoveField(
            model_name="board",
            name="filename",
        ),
        migrations.RemoveField(
            model_name="board",
            name="filesize",
        ),
        migrations.RemoveField(
            model_name="board",
            name="hit",
        ),
        migrations.RemoveField(
            model_name="board",
            name="idx",
        ),
        migrations.RemoveField(
            model_name="board",
            name="post_date",
        ),
        migrations.AddField(
            model_name="board",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="board",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=1,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="board",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="board",
            name="writer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
