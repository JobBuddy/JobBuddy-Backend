# Generated by Django 2.0.5 on 2019-08-11 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_companyinfo_company_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idd', models.IntegerField()),
            ],
        ),
    ]