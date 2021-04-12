# Generated by Django 3.2 on 2021-04-12 15:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=75)),
                ('separator', models.CharField(choices=[(',', 'Comma (,)'), (';', 'Semicolon (;)'), ('\t', 'Tabulation')], default=',', max_length=1)),
                ('string_character', models.CharField(choices=[('"', 'Double-quote (")'), ('*', 'Asterisk (*)'), ('|', 'Vertical bar (|)'), ('^', 'Caret (^)')], default='"', max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schemas', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'schema',
                'verbose_name_plural': 'schemas',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('R', 'Ready'), ('P', 'Processing'), ('F', 'Fail')], default='P', max_length=1)),
                ('rows', models.PositiveIntegerField(default=100, validators=[django.core.validators.MinValueValidator(1)])),
                ('csv_file', models.FileField(blank=True, upload_to='')),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datasets', to='schemas.schema')),
            ],
            options={
                'verbose_name': 'dataset',
                'verbose_name_plural': 'datasets',
                'ordering': ('created', 'rows'),
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('order', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(200)])),
                ('column_type', models.CharField(choices=[('FNAME', 'Full name'), ('JOB', 'Job'), ('EMAIL', 'Email'), ('DOMAIN', 'Domain name'), ('PHONE', 'Phone number'), ('COMPANY', 'Company name'), ('TEXT', 'Text'), ('INTEGER', 'Integer'), ('ADDRESS', 'Address'), ('DATE', 'Date')], max_length=50, verbose_name='Type')),
                ('integer_from', models.IntegerField(default=0, verbose_name='From')),
                ('integer_to', models.IntegerField(default=0, verbose_name='To')),
                ('text_len', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(500)])),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='schemas.schema')),
            ],
            options={
                'verbose_name': 'column',
                'verbose_name_plural': 'columns',
                'ordering': ('order', '-created'),
            },
        ),
    ]
