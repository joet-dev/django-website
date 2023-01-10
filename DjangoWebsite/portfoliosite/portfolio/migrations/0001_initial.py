# Generated by Django 4.1.5 on 2023-01-09 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_title', models.CharField(max_length=200)),
                ('item_date', models.DateTimeField(verbose_name='date published')),
                ('item_hits', models.IntegerField(default=0)),
                ('item_img_id', models.CharField(max_length=150)),
            ],
        ),
    ]