from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from buildapp.models import Sentence, Article

admin.site.register(Sentence)
admin.site.register(Article)
=======
from .models import Article
admin.site.register(Article);
>>>>>>> 07c13ec744692792fe17a0d883af27a0113a4fd6
