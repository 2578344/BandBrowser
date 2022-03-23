# Generated by Django 2.2.26 on 2022-03-13 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('genres', models.CharField(max_length=32)),
                ('commitment', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=128)),
                ('dateCreated', models.DateField(max_length=128)),
                ('numberOfPostsActive', models.IntegerField(default=0)),
                ('numberOfCurrentMembers', models.IntegerField(default=0)),
                ('numberOfPotentialMembers', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Bands',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('title', models.CharField(max_length=128)),
                ('publishDate', models.DateField(max_length=128)),
                ('expireDate', models.DateField()),
                ('experienceRequired', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=32)),
                ('genre', models.CharField(max_length=32)),
                ('commitment', models.CharField(max_length=32)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BandBrowser.Band')),
            ],
        ),
    ]