# Generated by Django 4.2.6 on 2023-10-25 08:30

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('adresse', models.CharField(max_length=255, null=True)),
                ('photo', models.ImageField(null=True, upload_to='media/photo')),
                ('biographie', models.TextField(null=True)),
                ('centre', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Amis',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('primuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prim', to=settings.AUTH_USER_MODEL)),
                ('seconuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secon', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appartenir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Groupes',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(null=True, upload_to='media/photo_groupe')),
                ('code_groupe', models.CharField(max_length=250, null=True, unique=True)),
                ('membres', models.ManyToManyField(related_name='groupes_appartenus', through='testagora.Appartenir', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('lecture', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('amis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testagora.amis')),
                ('destinate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receveur', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='envoyeur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
                ('file', models.FileField(null=True, upload_to='media/document')),
                ('lecture', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('destinate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destinate', to=settings.AUTH_USER_MODEL)),
                ('destinategroup', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destinategroup', to='testagora.groupes')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='appartenir',
            name='groupe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appartenances', to='testagora.groupes'),
        ),
        migrations.AddField(
            model_name='appartenir',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appartenances', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='users',
            name='groupes',
            field=models.ManyToManyField(related_name='membre', through='testagora.Appartenir', to='testagora.groupes'),
        ),
        migrations.AddField(
            model_name='users',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='users',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
