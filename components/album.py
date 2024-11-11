import eyed3 # type: ignore
class Album:
    def __init__(self, album_name, cover, song_list):
        self.album_name = album_name
        self.cover = cover
        self.band = None
        self.song_list = song_list
        self.songs_data_list = []
        for song in song_list:
            song_data= None
            audio_file = eyed3.load(song)

            duration_seconds = audio_file.info.time_secs
            if not duration_seconds:
                duration_minutes = 0
                remaining_seconds = 0
            duration_minutes = int(duration_seconds // 60)
            remaining_seconds = int(duration_seconds % 60)

            song_title = audio_file.tag.title
            if not song_title:
                song_title = song.split("\\")[-1]
                for file_extension in [".mp3", ".flac", ".wav", ".ogg"]:
                    if song_title.endswith(file_extension):
                        song_title = song_title.replace(file_extension, "")
                        break

            track_num = audio_file.tag.track_num
            track_number = 0
            if track_num[0]:
                track_number = track_num[0]

            song_data = {"title":str(song_title),"duration":float(str(duration_minutes)+"."+str(f"{remaining_seconds:02d}")),"number":int(track_number)} 
            self.songs_data_list.append(song_data)