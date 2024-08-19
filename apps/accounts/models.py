from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from ..games.models import Games
from ..streams.models import Stream, Clip


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField('Никнейм', max_length=50, unique=True)
    email = models.EmailField('Почта', unique=True)
    avatar = models.ImageField('Аватар', upload_to='avatars/', null=True, blank=True)
    status = models.CharField('Статус', max_length=100, null=True, blank=True)
    download_games = models.ManyToManyField('games.Games', related_name='download_users', blank=True)
    friends_online = models.ManyToManyField('self', related_name='user_friends_online', symmetrical=False, blank=True)
    live_streams = models.ManyToManyField('streams.Stream', related_name='user_live_streams', blank=True)
    clips = models.ManyToManyField('streams.Clip', related_name='user_clips', blank=True)

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'