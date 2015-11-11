# -*- coding: utf-8 -*-
from django.db import models

class Document(models.Model):
    userImage = models.FileField(
    	upload_to='documents/',
    	)