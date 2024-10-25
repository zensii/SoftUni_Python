class Song:
    def __init__(self, name: str, length: float, single: bool):
        self.single = single
        self.length = length
        self.name = name

    def get_info(self):
        return f"{self.name} - {self.length}"

if __name__ == '__main__':
    song = Song("Running in the 90s", 3.45, False)
    print(song.get_info())
    second_song = Song("Around the World", 2.34, False)
    print(second_song.get_info())
