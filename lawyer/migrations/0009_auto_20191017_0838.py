# Generated by Django 2.2.6 on 2019-10-17 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lawyer', '0008_practice_area_sub_practice_area'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lawyer',
            options={'verbose_name_plural': 'Lawyers'},
        ),
        migrations.AlterModelOptions(
            name='practice_area',
            options={'verbose_name_plural': 'Practice_area'},
        ),
        migrations.AlterModelOptions(
            name='sub_practice_area',
            options={'verbose_name_plural': 'Sub_practice_area'},
        ),
        migrations.AlterField(
            model_name='sub_practice_area',
            name='state',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='lawyer.State'),
        ),
    ]
