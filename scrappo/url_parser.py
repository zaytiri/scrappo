import os

from scrappo.utils.file import File


class UrlParser:
    def __init__(self, urls):
        self.urls = urls

    def parse(self):

        if not os.path.isfile(self.urls[0]):
            return self.urls

        try:
            urls_file = File(self.urls[0])

            urls = []
            urls_found = []

            for url in urls_file.get_lines():
                url = url.rstrip()
                if not url:
                    urls.append(urls_found)
                    urls_found = []
                    continue
                else:
                    info = url.split(':::')
                    if len(info) > 1:
                        url = {'name': info[0], 'url': info[1]}
                    else:
                        url = {'name': '', 'url': info[0]}
                    urls_found.append(url)

            if len(urls_found) != 0:
                urls.append(urls_found)

            return urls

        except FileNotFoundError:
            raise SystemError(self.urls + ' was not found.')
