# Generated by Django 4.2.4 on 2023-08-24 10:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("skill", "0001_initial"),
        ("auth_r", "0003_alter_user_role_alter_user_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="bio",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="user",
            name="skills",
            field=models.ManyToManyField(to="skill.skill"),
        ),
    ]
