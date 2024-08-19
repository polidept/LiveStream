from django.db import models


class Stream(models.Model):
    title = models.CharField('Название стрима', max_length=100)
    description = models.TextField('Описание стрима')
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)
    streamer = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='user_streams')
    game = models.ForeignKey('games.Games', on_delete=models.CASCADE, related_name='game_streams')
    live = models.BooleanField('В эфире', default=False)
    live_url = models.URLField('Ссылка на стрим', blank=True, null=True)
    viewers = models.PositiveIntegerField('Просмотры', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стрим'
        verbose_name_plural = 'Стримы'


class Clip(models.Model):
    title = models.CharField('Название клипа', max_length=100)
    description = models.TextField('Описание клипа')
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)
    streamer = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='user_clips')
    stream = models.ForeignKey('streams.Stream', on_delete=models.CASCADE, related_name='stream_clips')
    clip_url = models.URLField('Ссылка на клип')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Клип'
        verbose_name_plural = 'Клипы'





