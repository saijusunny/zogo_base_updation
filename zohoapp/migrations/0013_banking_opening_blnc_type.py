# Generated by Django 4.0.2 on 2023-05-25 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0012_alter_banking_bd_bnk_det_alter_banking_mail_addr'),
    ]

    operations = [
        migrations.AddField(
            model_name='banking',
            name='opening_blnc_type',
            field=models.CharField(blank=True, default='', max_length=220, null=True),
        ),
    ]