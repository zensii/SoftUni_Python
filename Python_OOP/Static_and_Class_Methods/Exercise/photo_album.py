from math import ceil
from typing import List


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [ [] for _ in range(pages) ]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        needed_pages = ceil(photos_count / 4)
        return PhotoAlbum(needed_pages)

    def add_photo(self, label: str):
        for index, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PHOTOS_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {index+1} slot {len(page)+1}"

        return "No more free slots"

    def display(self):
        result = '-----------\n'
        for page in self.photos:
            result += ' '.join('[]' for pos in page if pos != '') + '\n'
            result += '-----------\n'
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
