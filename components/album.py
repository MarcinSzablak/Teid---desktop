import eyed3  # type: ignore
import io


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
            audio_file = eyed3.load(song_uri)
            if not audio_file or not audio_file.tag:
                raise ValueError(f"Unable to read or parse metadata for file: {song_uri}")

            # Extract cover image data if available
            if not self.cover:
                for frame in audio_file.tag.frame_set.get(b'APIC', []):
                    if frame.image_data:
                        self.cover = io.BytesIO(frame.image_data)
                        break

            # Calculate song duration in minutes and seconds
            duration_seconds = int(audio_file.info.time_secs) if audio_file.info.time_secs else 0
            duration_minutes, remaining_seconds = divmod(duration_seconds, 60)

            # Extract title and sanitize it if missing
            song_title = audio_file.tag.title or self._sanitize_filename(song_uri)

            # Extract track number
            track_number = audio_file.tag.track_num[0] if audio_file.tag.track_num else 0

            # Append song data
            self.songs_data_list.append({
                "title": str(song_title),
                "duration": float(f"{duration_minutes}.{remaining_seconds:02d}"),
                "number": track_number,
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
