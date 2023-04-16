import os

from scrappo.downloader import Downloader
from scrappo.utils.log import show


class Movies:
    def __init__(self, urls, output):
        self.urls = urls
        self.output = output

    def download(self):
        errors = []

        # returns a flat list
        urls = [item for sublist in self.urls for item in sublist]

        show('Downloading movies...')
        for index, movie in enumerate(urls):
            name = movie['name']
            url = movie['url']
            if not name:
                name = 'movie' + str(index+1)

            path = os.path.join(self.output, name + '.mp4')
            if os.path.isfile(path):
                show('Skipping existing video...')
                continue

            successful = Downloader(url, path)

            if not successful:
                error = {'path': path, 'url': url}
                errors.append(error)

        return errors
