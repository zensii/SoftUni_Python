from project_07.album import Album
from project_07.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for album in self.albums:
            if album.name == album_name:
                if album.published:
                    return f"Album has been published. It cannot be removed."
                self.albums.remove(album)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        return f"Band {self.name}\n" + '\n'.join([cur_album.details() for cur_album in self.albums])


if __name__ == '__main__':
    song = Song("Running in the 90s", 3.45, False)
    print(song.get_info())
    album = Album("Initial D", song)
    second_song = Song("Around the World", 2.34, False)
    print(album.add_song(second_song))
    print(album.details())
    print(album.publish())
    band = Band("Manuel")
    print(band.add_album(album))
    print(band.remove_album("Initial D"))
    print(band.details())