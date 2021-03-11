import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from urllib.parse import urlparse

class NotFoundException(Exception):
    pass


class TextComparer:
    def __init__(self, url_list):
        self.url_list = url_list
        self.file_names = []
        self.index = 0

    def download(self, url, filename):
        r = requests.get(url)
        if (not r.ok):
            raise NotFoundException

        dl_file = "books/" + filename
        with open(dl_file, "w") as f:
            f.write(r.text)

    def multi_download(self):
        for url in self.url_list:
            url_components = urlparse(url)
            for comp in url_components:
                path_elems = comp.split("/")
                for elem in path_elems:
                    if ".txt" in elem:
                        self.file_names.append(elem)

        with ThreadPoolExecutor() as ex:
            res = ex.map(self.download, self.url_list, self.file_names)
            return list(res)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.file_names[self.index]
        except IndexError:
            self.index = 0
            raise StopIteration
        self.index += 1
        return result

    def urllist_generator(self):
        for url in self.url_list:
            yield url

    def avg_vowels(self, text):
        vowels = "aeiouAEIOU"
        num_words = 0
        num_vowels = 0

        with open("books/" + text, "r") as f:
            text_lines = f.readlines()

        for line in text_lines:
            words = line.split(" ")
            num_words += len(words)

            for char in line:
                if char in vowels:
                    num_vowels += 1

        return {"name": text, "avg_vowels": num_vowels/num_words} 

    def hardest_read(self):
        with ProcessPoolExecutor() as ex:
            res = list(ex.map(self.avg_vowels, self.file_names))

            avg_v_counts = [book["avg_vowels"] for book in res]
            hardest_book = [book for book in res if book["avg_vowels"] == max(avg_v_counts)]

            # hardest_book becomes a list, so I just return the first (and only) element of that list
            return hardest_book[0]






