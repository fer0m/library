# Generated by Django 3.1.3 on 2020-11-14 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='books_in_reserve',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='library.book'),
        ),
    ]
