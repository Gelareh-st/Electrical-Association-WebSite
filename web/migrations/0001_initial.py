# Generated by Django 4.0.2 on 2022-04-06 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique_for_month=True, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='Last Name')),
                ('category', models.CharField(choices=[('Member', 'Member'), ('Faculty', 'Faculty'), ('Staff', 'Staff')], default='Faculty', max_length=30, verbose_name='Category')),
                ('Picture_URL', models.URLField(verbose_name='Picture')),
                ('EmailAddress', models.EmailField(max_length=254, verbose_name='Email')),
                ('LinkedIn', models.URLField(blank=True, max_length=80)),
                ('GitHub', models.URLField(blank=True, max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('people_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='web.people')),
                ('Resume_Link', models.URLField(verbose_name='Resume Link')),
                ('Performance_result', models.IntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], verbose_name='Performance')),
            ],
            bases=('web.people',),
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('people_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='web.people')),
            ],
            bases=('web.people',),
        ),
    ]