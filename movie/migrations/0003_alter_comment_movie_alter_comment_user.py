# Generated by Django 4.2.7 on 2024-02-04 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('movie', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.movie'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.account'),
        ),
    ]
