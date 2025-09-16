from django.contrib import admin
from apps.movies.models import( Movie, Language,Genre,Country,MovieSubtitle,MovieAudio,
                               MovieFile,PosterImage,MovieAudio,WatchSession)


admin.site.register(Movie)
admin.site.register(Language)
admin.site.register(MovieFile)
admin.site.register(Country)
admin.site.register(MovieSubtitle)
admin.site.register(PosterImage)
admin.site.register(Genre)
admin.site.register(MovieAudio)
admin.site.register(WatchSession)
