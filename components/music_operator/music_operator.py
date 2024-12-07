import pygame

class Music_Operator:
    source = None
    pygame.mixer.init()
    
    @staticmethod
    def play_music():
        pygame.mixer.music.load(Music_Operator.source)
        pygame.mixer.music.play()

    @staticmethod
    def set_music_value(value):
        pygame.mixer.music.set_volume(value)

    @staticmethod
    def pause_music():
        pygame.mixer.music.pause()
    
    @staticmethod
    def unpause_music():
        pygame.mixer.music.unpause()