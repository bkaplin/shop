# -*- coding: utf-8 -*-
from django.db import models

class Clothes(models.Model):
	name = models.CharField(max_length = 255)
	color = models.CharField(max_length = 12, choices=(('B', 'Black'), 													('D', 'Dark blue')))
	image_number = models.IntegerField()
	size = models.CharField(max_length = 3, choices=(('48', '48'),('50', '50'),  										('52', '52'), ('54', '54'),  											('56', '56'), ('58', '58')))
	short_description = models.CharField(max_length = 255, help_text = 							u'краткое описание', null = True, blank = True)
	description = models.TextField(help_text = u'полное описание', 										null = True, blank = True)
	def __unicode__(self):
		return self.name
