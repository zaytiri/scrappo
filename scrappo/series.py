import os

from scrappo.downloader import Downloader
from scrappo.utils.log import show
from scrappo.video import Video


class Series(Video):
    def __init__(self, urls, output):
        super().__init__(urls, output)

    def process_urls(self):
        show('Downloading serie...')
        for i, season in enumerate(self.urls):
            season_folder = self.add_folder('season' + str(i+1))

            for j, episode in enumerate(season):
                url = episode['url']
                name = self.resolve_video_name(episode['name'], 'episode' + str(j + 1))

                path = os.path.join(season_folder, name + '.mp4')
                if self.file_exists(path):
                    continue

                successful = Downloader(url, path)

                self.add_errors(successful, path, url)
