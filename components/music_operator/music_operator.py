import pygame

class Music_Operator:
    source = None
    song_index = None
    album = None
    is_paused = False
    pygame.mixer.init()
    
    @staticmethod
    def play_music():
        pygame.mixer.music.load(Music_Operator.source)
        pygame.mixer.music.play()
        if pygame.mixer.music.get_busy():
            Music_Operator.unpause_music()

    @staticmethod
    def is_busy():
        return pygame.mixer.music.get_busy()

    @staticmethod
    def set_music_value(value):
        pygame.mixer.music.set_volume(value)

    @staticmethod
    def pause_music():
        pygame.mixer.music.pause()
        Music_Operator.is_paused = True
    
    @staticmethod
    def unpause_music():
        pygame.mixer.music.unpause()
        Music_Operator.is_paused = False

    @staticmethod
    def get_song_index():
        if Music_Operator.album != None:
            for song in Music_Operator.album.songs_data_list:
                if song["url"]==Music_Operator.source:
                    Music_Operator.song_index = Music_Operator.album.songs_data_list.index(song)