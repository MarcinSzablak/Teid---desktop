class Album:
    def __init__(self, album_name, cover, song_list):
        self.album_name = album_name
        self.cover = cover
        self.song_list = song_list
        self.band= None

        # print(f"Album: {self.album_name}")
        # print(f"Cover: {self.cover}")
        # print("Songs:")
        # for song in self.song_list:
        #     print(f"  - {song}")