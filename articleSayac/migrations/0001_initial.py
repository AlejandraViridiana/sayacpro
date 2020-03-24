# Generated by Django 2.2.6 on 2020-02-23 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userSayac', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameMagazine', models.CharField(max_length=50, verbose_name='Nombre de revista')),
                ('editMagazine', models.CharField(max_length=50, verbose_name='Editorial')),
                ('countryMagazine', models.CharField(max_length=50, verbose_name='País')),
                ('quartMagazine', models.CharField(choices=[(None, 'Selecciona estado'), (' q1 ', ' q1 '), (' q2 ', ' q2 '), (' q3 ', ' q3 '), (' q4 ', ' q4 ')], max_length=25, verbose_name='Cuartiles')),
                ('referenceMagazine', models.CharField(max_length=100, verbose_name='Enlace a revista')),
                ('indMagazine', models.BooleanField(verbose_name='Indizado')),
                ('indexedMagazine', models.CharField(max_length=50, verbose_name='Índice en que se encuentra')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otherUserInArticle', models.TextField(max_length=220, verbose_name='Co-autores')),
                ('topicArticle', models.CharField(choices=[(None, 'Selecciona estado'), (' Medicina ', ' Medicina '), (' Inteligencia Artificial', 'Inteligencia Artificial')], max_length=25, verbose_name='Tema')),
                ('titleArticle', models.CharField(max_length=50, verbose_name='Título de artículo')),
                ('pagesArticle', models.CharField(max_length=50, verbose_name='Páginas donde está publicado')),
                ('estatusArticle', models.CharField(choices=[(None, 'Selecciona estado'), ('En proceso', 'En proceso'), ('Sometido', 'Sometido'), ('Liberado', 'Liberado')], max_length=25, verbose_name='Estatus')),
                ('volArticle', models.CharField(default=' N/A ', max_length=50, verbose_name='Volumen')),
                ('doiArticle', models.CharField(default=' - ', max_length=50, verbose_name='DOI')),
                ('archArticle', models.FileField(blank=True, upload_to='archiving/', verbose_name='Archivo (PDF) de articulo')),
                ('createdPubArticle', models.DateTimeField(auto_now_add=True)),
                ('magazineArticle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='articleSayac.Magazine', verbose_name='Nombre de revista')),
                ('projectArticle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.Project', verbose_name='Proyecto')),
                ('userArticle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='userSayac.User', verbose_name='Autor principal')),
            ],
        ),
    ]
