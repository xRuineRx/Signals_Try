from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# для загрузки фото и видео
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


# Create your models here.


#Для индификации юзера при отправке откликов
class GameUser(models.Model):
    user_link = models.OneToOneField(User, on_delete=models.CASCADE)


# class GameCategory(models.Model):
#     text = models.CharField(max_length=100)

class GamePost(models.Model):
    header = models.CharField(max_length=100, unique= True)
    text = models.TextField()
    text_picture = models.TextField(blank=True)
    body = RichTextUploadingField(blank=True, config_name='default')

    #Опишем ограниченный выбор категорий
    class GameCategory(models.TextChoices):
        Cat_1 ='TANK', 'Танки'
        Cat_2 ='HEAL', 'Хилы'
        Cat_3 ='DD', 'ДД'
        Cat_4 ='TRADE', 'Торговцы'
        Cat_5 ='GUILDM', 'Гилдмастеры'
        Cat_6 ='QUESTGV', 'Квестгиверы'
        Cat_7 ='KZ', 'Кузнецы'
        Cat_8 ='LETHER', 'Кожевники'
        Cat_9 ='Alch', 'Зельевары'
        Cat_10 ='MAGIC', 'Мастера заклинаний'

    CategoryCheck = models.CharField(blank=True, choices=GameCategory.choices, max_length = 100)

    #связи MtM
    link_GameUser = models.ForeignKey(GameUser, on_delete=models.CASCADE)

    #Функция для отправки отклика на объявление
    game_message_senders = models.ManyToManyField(User, blank=True, null=True)



#Сообщения пользователей
# class GameMessage(models.Model):
#     text = models.TextField()
#     user_link = models.OneToOneField(User, on_delete=models.CASCADE)


# class PostCategory(models.Model):
#     #otm = OneToMany
#     link_otm_Post = models.ForeignKey(GamePost, on_delete=models.CASCADE)