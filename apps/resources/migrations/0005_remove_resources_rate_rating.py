# Generated by Django 4.2.4 on 2023-08-30 08:29

import apps.resources.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resources', '0004_alter_category_options_alter_resources_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resources',
            name='rate',
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('rate', models.IntegerField(validators=[apps.resources.validators.check_rating_range])),
                ('resources_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.resources')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
