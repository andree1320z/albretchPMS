# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
        ('physician', '0001_initial'),
        ('hospital', '0004_auto_20171117_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ct_area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=100)),
                ('severity', models.CharField(max_length=100)),
                ('date_of_diagnosis', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=None, verbose_name='Active?')),
                ('remarks', models.TextField(default='None', help_text='Any Other Remarks', max_length=1000)),
                ('icd_10', models.CharField(blank=True, max_length=100, null=True, verbose_name='ICD 10')),
            ],
        ),
        migrations.CreateModel(
            name='Medical_history_sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chief_complain', models.CharField(default='insert value', max_length=200)),
                ('history_of_present_illness', models.CharField(default='insert value', max_length=200)),
                ('pass_diseases_history', models.CharField(default='insert value', max_length=200)),
                ('current_drug_theraphy_and_other_addiction', models.CharField(default='insert value', max_length=200)),
                ('allergy_to', models.CharField(default='insert value', max_length=200)),
                ('family_history', models.CharField(default='insert value', max_length=200)),
                ('summary', models.TextField(default='insert value')),
                ('primary_dx', models.TextField(default='insert value')),
                ('attending_physician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_history_sheets', to='physician.Physician')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_addmition', models.DateField()),
                ('date_of_discharge', models.DateField(blank=True, null=True)),
                ('open', models.BooleanField(default=0)),
                ('ward', models.CharField(max_length=4)),
                ('room', models.CharField(max_length=4)),
                ('bed', models.CharField(max_length=2)),
                ('parent_hospital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.Hospital')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_file', to='patient.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='MedicationList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication', models.CharField(help_text='Only Generic Names..', max_length=100)),
                ('strength', models.CharField(max_length=100)),
                ('dosage', models.CharField(help_text='OD, BD, TDS, QID, HS, SOS, PID etc..', max_length=100)),
                ('prescription_date', models.DateField()),
                ('prescribed_by', models.CharField(choices=[('internal', 'Internal Doctor'), ('external', 'External Doctor')], default='Internal', max_length=100)),
                ('currently_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mri_area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('order', models.CharField(default='insert value', max_length=200)),
                ('physician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='physician.Physician')),
            ],
        ),
        migrations.CreateModel(
            name='Physician_order_sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('attending_physician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='physician.Physician')),
                ('medical_file', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='physician_order_sheet', to='history_records.MedicalFile')),
            ],
        ),
        migrations.CreateModel(
            name='Progress_note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('treatment_progress', models.CharField(default='insert value', max_length=200)),
                ('physician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='physician.Physician')),
            ],
        ),
        migrations.CreateModel(
            name='Progress_notes_sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('attending_physician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='physician.Physician')),
                ('medical_file', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='progress_note_sheet', to='history_records.MedicalFile')),
            ],
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_condition_after_surgery', models.TextField(blank=True, max_length=500, null=True, verbose_name='Base Condition')),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('classification', models.CharField(max_length=200)),
                ('date_of_surgery', models.DateField()),
                ('healed', models.BooleanField(default=None)),
                ('remarks', models.TextField(default='None', help_text='Any Other Remarks', max_length=1000)),
                ('icd_10', models.CharField(blank=True, max_length=100, null=True, verbose_name='ICD10')),
                ('icd_10_pcs', models.CharField(blank=True, max_length=100, null=True, verbose_name='ICD10 PCS')),
            ],
        ),
        migrations.CreateModel(
            name='Test_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('desciption', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit_summary_sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chief_complaint_and_primary_diagnosis', models.CharField(default='insert value', max_length=200)),
                ('final_diagnosis', models.CharField(default='insert value', max_length=200)),
                ('medical_and_surgical_procedures', models.CharField(default='insert value', max_length=200)),
                ('results_of_paraclinical_examinations', models.CharField(default='insert value', max_length=200)),
                ('disease_progress', models.CharField(default='insert value', max_length=200)),
                ('patient_condition_on_discharge', models.CharField(default='insert value', max_length=200)),
                ('recommendations_after_discharge', models.CharField(default='insert value', max_length=200)),
                ('recommendations_for_family_physician', models.CharField(default='insert value', max_length=200)),
                ('attending_physician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_summaries', to='physician.Physician')),
                ('medical_file', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='unit_summary_sheet', to='history_records.MedicalFile')),
                ('other_physicians', models.ManyToManyField(related_name='summary_attend', to='physician.Physician')),
            ],
        ),
        migrations.CreateModel(
            name='X_ray_area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='X_ray_view',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ct',
            fields=[
                ('basedocument_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='history_records.BaseDocument')),
                ('image', models.ImageField(upload_to='cts')),
                ('description', models.CharField(choices=[('1', 'With injection'), ('0', 'Without injection')], max_length=20)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history_records.Ct_area')),
                ('historyFile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ct', to='history_records.MedicalFile')),
            ],
            bases=('history_records.basedocument',),
        ),
        migrations.CreateModel(
            name='Mri',
            fields=[
                ('basedocument_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='history_records.BaseDocument')),
                ('image', models.ImageField(upload_to='mris')),
                ('area', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='history_records.Mri_area')),
                ('historyFile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mri', to='history_records.MedicalFile')),
            ],
            bases=('history_records.basedocument',),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('basedocument_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='history_records.BaseDocument')),
                ('image', models.ImageField(upload_to='tests')),
                ('historyFile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test', to='history_records.MedicalFile')),
            ],
            bases=('history_records.basedocument',),
        ),
        migrations.CreateModel(
            name='X_ray',
            fields=[
                ('basedocument_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='history_records.BaseDocument')),
                ('image', models.ImageField(upload_to='x_rays')),
                ('kind_of_adm', models.CharField(choices=[('emg', 'Emergency'), ('hosp', 'Hosp.'), ('opd', 'O.P.D.')], max_length=10)),
                ('area', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='history_records.X_ray_area')),
                ('historyFile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='x_ray', to='history_records.MedicalFile')),
                ('view', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='history_records.X_ray_view')),
            ],
            bases=('history_records.basedocument',),
        ),
        migrations.AddField(
            model_name='progress_note',
            name='sheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='history_records.Progress_notes_sheet'),
        ),
        migrations.AddField(
            model_name='order',
            name='sheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='history_records.Physician_order_sheet'),
        ),
        migrations.AddField(
            model_name='medical_history_sheet',
            name='medical_file',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='medical_history_sheet', to='history_records.MedicalFile'),
        ),
        migrations.AddField(
            model_name='disease',
            name='disease_medication_list',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='history_records.MedicationList'),
        ),
    ]
