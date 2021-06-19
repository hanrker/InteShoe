# Generated by Django 3.2.4 on 2021-06-12 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iShoe', '0003_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoeTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creatime', models.DateField()),
                ('people', models.CharField(max_length=8)),
                ('infor', models.CharField(max_length=128)),
                ('metalshoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iShoe.metalshoe')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iShoe.tag')),
            ],
        ),
        migrations.AlterField(
            model_name='tag',
            name='shoeid',
            field=models.ManyToManyField(through='iShoe.ShoeTag', to='iShoe.MetalShoe'),
        ),
    ]
