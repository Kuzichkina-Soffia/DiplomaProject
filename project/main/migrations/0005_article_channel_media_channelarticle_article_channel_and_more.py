# Generated by Django 4.2.10 on 2024-02-19 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_chat_userchat_messageсhat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.standartuser')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ChannelArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.article')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.channel')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.channel'),
        ),
        migrations.CreateModel(
            name='VideoArticle',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.article')),
                ('video', models.OneToOneField(limit_choices_to={'file__startswith': 'videos'}, on_delete=django.db.models.deletion.CASCADE, related_name='video_articles', to='main.media')),
            ],
            bases=('main.article',),
        ),
        migrations.CreateModel(
            name='ImageArticle',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.article')),
                ('images', models.ManyToManyField(limit_choices_to={'file__startswith': 'images'}, related_name='image_articles', to='main.media')),
            ],
            bases=('main.article',),
        ),
        migrations.CreateModel(
            name='AudioArticle',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.article')),
                ('audios', models.ManyToManyField(limit_choices_to={'file__startswith': 'audios'}, related_name='audio_articles', to='main.media')),
            ],
            bases=('main.article',),
        ),
    ]
