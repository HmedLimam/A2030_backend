from django.contrib import admin
from .models import Event, Speaker, Session, Delegate, Blog, Score

admin.site.register(Delegate)
admin.site.register(Event)
admin.site.register(Speaker)
admin.site.register(Session)
admin.site.register(Blog)
admin.site.register(Score)