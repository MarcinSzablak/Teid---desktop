import eyed3  # type: ignore
from mutagen.flac import FLAC # type: ignore
from tinytag import TinyTag # type: ignore
import io
import os


class Album:
    def __init__(self, album_name, cover, song_list):
        """
        Initialize an album with metadata extracted from audio files.

        Args:
            album_name (str): The name of the album.
            cover (str or BytesIO): The path to the album cover or raw image data.
            song_list (list): A list of song file paths.
        """
        self.album_name = album_name
        self.cover = cover
        self.band = None
        self.song_list = song_list
        self.songs_data_list = []

        for song_uri in song_list:
            self._process_song(song_uri)

    def _process_song(self, song_uri):
        """
        Process metadata for a single song and add it to the album's song data list.

        Args:
            song_uri (str): The file path to the song.
        """ 
        try:
            metadata = self.get_file_metadata(song_uri)

            self.songs_data_list.append({
                "title": str(metadata[0]),
                "duration": str(f"{metadata[1]}.{metadata[2]:02d}"),
                "number": metadata[3],
                "url": str(song_uri)
            })

        except Exception as e:
            print(f"Error processing {song_uri}: {e}")

    @staticmethod
    def _sanitize_filename(file_path):
        """
        Extract a clean title from a file path.

        Args:
            file_path (str): The file path of the song.

        Returns:
            str: A sanitized title without file extensions.
        """
        file_name = file_path.split("/")[-1].split("\\")[-1]
        for file_extension in [".mp3", ".flac", ".wav", ".ogg"]:
            if file_name.lower().endswith(file_extension):
                return file_name[:-len(file_extension)]
        return file_name.strip()
    
    def get_file_metadata(self,song_uri):
        file_extension = os.path.splitext(song_uri)[1][1:].lower()
        match file_extension:
            case "mp3":
                audio_file = eyed3.load(song_uri)

                if not self.cover:
                    for frame in audio_file.tag.frame_set.get(b'APIC', []):
                        if frame.image_data:
                            self.cover = io.BytesIO(frame.image_data)
                            break

                duration_seconds = int(audio_file.info.time_secs) if audio_file.info.time_secs else 0
                duration_minutes, remaining_seconds = divmod(duration_seconds, 60)

                song_title = audio_file.tag.title or self._sanitize_filename(song_uri)

                self.band = audio_file.tag.artist or "None"

                if audio_file.tag.track_num[0]==None:
                    track_number=0
                else:
                    track_number = audio_file.tag.track_num[0]

                return(song_title,duration_minutes,remaining_seconds,track_number)
            case "flac":
                audio = FLAC(song_uri)
                for key, value in audio.items():
                    if(key=="title"):
                        song_title=value[0]
                    else:
                        song_title=self._sanitize_filename(song_uri)
                    
                    if(key=="artist"):
                        self.band=value[0]
                    else:
                        self.band="None"
                    
                    if(key=="tracknumber"):
                        track_number=value[0]
                    else:
                        track_number=0
                    
                duration_seconds = int(audio.info.length) if audio.info.length else 0
                duration_minutes, remaining_seconds = divmod(duration_seconds, 60)
                return(song_title,duration_minutes,remaining_seconds,track_number)
            case "wav":
                tag = TinyTag.get(song_uri)
                if(tag.title):
                    song_title=tag.title
                else:
                    song_title=self._sanitize_filename(song_uri)
                
                if(tag.artist):
                    self.band=tag.artist
                else:
                    self.band="None"
                duration_seconds = int(tag.duration) if tag.duration else 0
                duration_minutes, remaining_seconds = divmod(duration_seconds, 60)

                if(tag.track):
                        track_number=tag.track
                else:
                    track_number=0

                return(song_title,duration_minutes,remaining_seconds,track_number)
            case "ogg":
                tag = TinyTag.get(song_uri)
                if(tag.title):
                    song_title=tag.title
                else:
                    song_title=self._sanitize_filename(song_uri)
                
                if(tag.artist):
                    self.band=tag.artist
                else:
                    self.band="None"
                duration_seconds = int(tag.duration) if tag.duration else 0
                duration_minutes, remaining_seconds = divmod(duration_seconds, 60)

                if(tag.track):
                        track_number=tag.track
                else:
                    track_number=0

                return(song_title,duration_minutes,remaining_seconds,track_number)
            case _:
                return None
