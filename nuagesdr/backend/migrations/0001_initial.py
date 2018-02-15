# Generated by Django 2.0.2 on 2018-02-14 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnumFieldTypesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enum_value', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FieldTypesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=255, null=True)),
                ('field_type', models.CharField(max_length=10, null=True)),
            ],
            options={
                'ordering': ['field_name'],
            },
        ),
        migrations.CreateModel(
            name='RiskTypesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_type_name', models.CharField(max_length=255, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='fieldtypesmodel',
            name='risktype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_info', to='backend.RiskTypesModel'),
        ),
        migrations.AddField(
            model_name='enumfieldtypesmodel',
            name='fieldtypes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enum_value', to='backend.FieldTypesModel'),
        ),
        migrations.AlterUniqueTogether(
            name='fieldtypesmodel',
            unique_together={('risktype', 'field_name', 'field_type')},
        ),
    ]
