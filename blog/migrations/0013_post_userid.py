# Generated by Django 3.0.3 on 2020-02-05 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_usersignup'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='userid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.Usersignup'),
            preserve_default=False,
        ),
    ]