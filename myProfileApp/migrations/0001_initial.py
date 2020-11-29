# Generated by Django 3.1.3 on 2020-11-29 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myLoginApp', '0001_initial'),
        ('myRecipeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('FolderId', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Unique FolderId')),
                ('Name', models.CharField(max_length=200, verbose_name='Name')),
                ('Position', models.PositiveSmallIntegerField(verbose_name='Position')),
                ('FolderIdParent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myProfileApp.folder', verbose_name='Parent Folder')),
            ],
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('FavouriteId', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Unique FavouriteId')),
                ('Note', models.TextField(verbose_name='Note')),
                ('NumberPeople', models.PositiveSmallIntegerField(verbose_name='Number of People')),
                ('Position', models.PositiveSmallIntegerField(verbose_name='Position')),
                ('FolderId', models.ForeignKey(on_delete=models.SET(1), to='myProfileApp.folder', verbose_name='Folder')),
                ('RecipeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myRecipeApp.recipe', verbose_name='Recipe')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myLoginApp.user', verbose_name='Owner')),
            ],
        ),
    ]
