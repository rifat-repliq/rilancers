# Generated by Django 4.2.4 on 2023-08-27 04:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("skill", "0002_alter_skill_title"),
        ("auth_r", "0004_user_bio_user_skills"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="skills",
            field=models.ManyToManyField(blank=True, to="skill.skill"),
        ),
    ]
