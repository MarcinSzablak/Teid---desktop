import pygame

class Music_Operator:
    source = None
    song_index = None
    album = None
    is_paused = False
    pygame.mixer.init()

    observers = []

    @staticmethod
    def add_observer(observer):
        """Adds an observer to the list."""
        Music_Operator.observers.append(observer)

    @staticmethod
    def notify_observers(new_info,**args):
        """Notifies all observers of the filter change."""
        for observer in Music_Operator.observers:
            observer(new_info)
    
    @staticmethod
    def play_music():
        pygame.mixer.music.load(Music_Operator.source)
        pygame.mixer.music.play()
        Music_Operator.unpause_music()

    @staticmethod
    def set_music_value(value):
        pygame.mixer.music.set_volume(value)

    @staticmethod
    def is_busy():
        return pygame.mixer.music.get_busy()

    @staticmethod
    def pause_music():
        pygame.mixer.music.pause()
        Music_Operator.is_paused = True
        Music_Operator.notify_observers(Music_Operator.is_paused)
    
    @staticmethod
    def unpause_music():
        pygame.mixer.music.unpause()
        Music_Operator.is_paused = False
        Music_Operator.notify_observers(Music_Operator.is_paused)

    @staticmethod
    def get_song_index():
        if Music_Operator.album != None:
            for song in Music_Operator.album.songs_data_list:
                if song["url"]==Music_Operator.source:
                    Music_Operator.song_index = Music_Operator.album.songs_data_list.index(song)