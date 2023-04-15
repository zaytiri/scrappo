import os

from scrappo.downloader import Downloader
from scrappo.utils.log import show


class Series:
    def __init__(self, urls, output):
        self.urls = urls
        self.output = output

    def download(self):
        errors = []

        show('Downloading serie...')
        for i, season in enumerate(self.urls):
            season_folder = os.path.join(self.output, 'season' + str(i+1))
            if not os.path.isdir(season_folder):
                os.mkdir(season_folder)

            for j, episode in enumerate(season):
                name = episode['name']
                url = episode['url']
                if not name:
                    name = 'episode' + str(j+1)

                path = os.path.join(season_folder, name + '.mp4')
                if os.path.isfile(path):
                    show('Skipping existing video...')
                    continue

                successful = Downloader(url, path)

                if not successful:
                    error = {'path': path, 'url': url}
                    errors.append(error)

        return errors
