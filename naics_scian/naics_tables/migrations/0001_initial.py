# Generated by Django 3.1.1 on 2020-09-09 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NAICSClassification',
            fields=[
                ('code', models.CharField(help_text='Code for the classification', max_length=10, primary_key=True, serialize=False)),
                ('level', models.PositiveIntegerField(help_text='Nesting level in the hierarchy')),
                ('structure', models.CharField(choices=[('Sector', 'Sector'), ('Subsector', 'Subsector'), ('Industry group', 'Industry Group'), ('Industry', 'Industry'), ('Canadian industry', 'Canadian Industry')], help_text='Corresponding structure', max_length=17)),
                ('class_title', models.CharField(max_length=200)),
                ('superscript', models.CharField(blank=True, choices=[('CAN', 'CAN'), ('US', 'US'), ('MEX', 'MEX')], help_text='Used to signify comparability', max_length=3)),
                ('class_definition', models.TextField()),
                ('parent', models.ForeignKey(blank=True, default=None, help_text='Parent classification (null if top-level)', null=True, on_delete=django.db.models.deletion.CASCADE, to='naics_tables.naicsclassification')),
            ],
            options={
                'verbose_name': 'NAICS Classification',
                'ordering': ('code',),
            },
        ),
    ]
