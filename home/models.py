# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Aluno(models.Model):

    #__Aluno_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)

    #__Aluno_FIELDS__END

    class Meta:
        verbose_name        = _("Aluno")
        verbose_name_plural = _("Aluno")


class Professor(models.Model):

    #__Professor_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)

    #__Professor_FIELDS__END

    class Meta:
        verbose_name        = _("Professor")
        verbose_name_plural = _("Professor")


class Disciplina(models.Model):

    #__Disciplina_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)

    #__Disciplina_FIELDS__END

    class Meta:
        verbose_name        = _("Disciplina")
        verbose_name_plural = _("Disciplina")



#__MODELS__END
