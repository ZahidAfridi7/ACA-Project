from django.contrib import admin
from .models import Player,PlayerList,PlayerRole,About,Feedback
# Register your models here.
admin.site.register(Player)
admin.site.register(PlayerRole)
admin.site.register(PlayerList)
admin.site.register(About)
admin.site.register(Feedback)