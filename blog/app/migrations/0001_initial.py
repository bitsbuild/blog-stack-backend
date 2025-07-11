# Generated by Django 5.2.3 on 2025-06-24 15:27

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('blog_title', models.CharField(max_length=150)),
                ('blog_body', models.CharField(max_length=7500)),
                ('blog_created', models.DateTimeField(auto_now_add=True)),
                ('blog_updated', models.DateTimeField(auto_now=True)),
                ('blog_writer', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('blog_categories', models.ManyToManyField(related_name='blogs', to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('review_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('review_title', models.CharField(max_length=150)),
                ('review_body', models.CharField(max_length=1500)),
                ('review_created', models.DateTimeField(auto_now_add=True)),
                ('review_updated', models.DateTimeField(auto_now=True)),
                ('for_blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='app.blog')),
                ('review_writer', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
