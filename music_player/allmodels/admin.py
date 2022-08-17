# Register your models here.
from django.contrib import admin

from .models.album import Album, AlbumLikes, AlbumReleaseInfo, Country, Genre
from .models.artist import Artist, ArtistPhotos
from .models.auto_playlists import History, LikedSong
from .models.event import Event
from .models.others import Track, TrackLikes
from .models.playlist import (
    Playlist,
    PlaylistContent,
    PlaylistLikes,
    PlaylistParticipants,
)
from .models.user import User

admin.site.register(User)
admin.site.register(Album)
admin.site.register(Country)
admin.site.register(AlbumReleaseInfo)
admin.site.register(AlbumLikes)
admin.site.register(ArtistPhotos)
admin.site.register(Artist)
admin.site.register(LikedSong)
admin.site.register(History)
admin.site.register(Event)
admin.site.register(Genre)
admin.site.register(Track)
admin.site.register(TrackLikes)
admin.site.register(Playlist)
admin.site.register(PlaylistLikes)
admin.site.register(PlaylistContent)
admin.site.register(PlaylistParticipants)
