# Generated by Django 2.1 on 2020-12-01 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='mensagem',
            new_name='mensagem_contato',
        ),
    ]
