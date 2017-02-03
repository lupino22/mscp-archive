from __future__ import unicode_literals

from django.db import models

class Game(models.Model):
    id = models.AutoField('id', primary_key=True, db_index=True)
    name = models.CharField(max_length=300, verbose_name="Тоглоомын нэр")
    link = models.CharField(max_length=300, verbose_name="Холбоос")

class Replay(models.Model):
    id = models.AutoField('id', primary_key=True, db_index=True)
    createdDate = models.DateTimeField(verbose_name="Огноо", auto_now_add=False)
    has_game = models.ManyToOneRel(Game, verbose_name="Тоглоом", blank=True)
    has_players = models.ManyToManyField(Player, verbose_name="Тоглогч", blank=True)

class Video(models.Model):
    id = models.AutoField('id', primary_key=True, db_index=True)
    nick = models.CharField(max_length=300, verbose_name="Гарчиг")
    desc = models.TextField(verbose_name="Тухай")
    createdDate = models.DateTimeField(verbose_name="Огноо", auto_now_add=False)
    has_game = models.ManyToOneRel(Game, verbose_name="Тоглоом", blank=True)
    has_players = models.ManyToManyField(Player, verbose_name="Тоглогч", blank=True)
    has_caster = models.ManyToManyField(Player, related_name="caster", verbose_name="Тайлбарлагч", blank=True)

class Player(models.Model):
    id = models.AutoField('id', primary_key=True, db_index=True)
    nick = models.CharField(max_length=300, verbose_name="Тоглогчийн нэр")
    preNick = models.CharField(max_length=300, verbose_name="бусад IDs", blank=True)
    realName = models.CharField(max_length=300, verbose_name="Жинхэнэ нэр", blank=True)
    avatar = models.ImageField(verbose_name="Аватар", upload_to='/avatar', blank=True)
    has_games = models.ManyToManyField(Game, verbose_name="Тоглосон тоглоомууд")
    has_imgs = models.ManyToManyField(Images, verbose_name="Зурагууд")

class Tournament(models.Model):
    id = models.AutoField('id', primary_key=True, db_index=True)
    name = models.CharField(max_length=300, verbose_name="Тэмцээний нэр")
    hostedDate = models.CharField(verbose_name="Огноо", blank=True)
    desc = models.TextField(verbose_name="Тэмцээний мэдээлэл")
    has_players = models.ManyToManyField(Player, verbose_name="Тоглогч")
    has_imgs = models.ManyToManyField(Images, verbose_name="Зурагууд")

class Images(models.Model):
    id = models.AutoField('id', primary_key=True, db_index=True)
    imgCode = models.CharField(max_length=300, verbose_name="Зурагийн код")
    img = models.ImageField(verbose_name="Зураг", upload_to='/pictures', blank=True)




