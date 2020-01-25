from django.contrib import admin
from . import models

class CompanyAdmin(admin.ModelAdmin):
	list_display = (
		'name',
	)

class ConsoleAdmin(admin.ModelAdmin):
	list_display = (
		'name',
		'company',
	)

class GameAdmin(admin.ModelAdmin):
	list_display = (
		'title',
		'release_date',
		'console',
	)

admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.Console, ConsoleAdmin)
admin.site.register(models.Game, GameAdmin)
