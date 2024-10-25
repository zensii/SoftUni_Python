from typing import List, Tuple
from project_07.song import Song


class Album:
    def __init__(self, name: str, *args: [Tuple[Song], Song]):
        self.name = name
        self.published = False
        self.songs = []
        for arg in args:
            if isinstance(arg, tuple):
                self.songs.extend(arg)
            else:
                self.songs.append(arg)

    def add_song(self, song: Song):
        if song in self.songs:
            return f"Song is already in the album."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        for song in self.songs:
            if song.name == song_name:
                if self.published:
                    return f"Cannot remove songs. Album is published."
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
        return f"Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        return f"Album {self.name}\n" + '\n'.join([f"== {cur_song.get_info()}" for cur_song in self.songs])

if __name__ == '__main__':
    song = Song("Running in the 90s", 3.45, False)
    print(song.get_info())
    album = Album("Initial D", song)
    second_song = Song("Around the World", 2.34, False)
    print(album.add_song(second_song))
    print(album.details())
    print(album.publish())
