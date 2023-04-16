import os

from scrappo.utils.file import File


class UrlParser:
    def __init__(self, urls):
        self.urls = urls

    def parse(self):
        if not os.path.isfile(self.urls[0]):
            return self.parse_urls(self.urls)

        try:
            urls_file = File(self.urls[0])
            return self.parse_urls(urls_file.get_lines())

        except FileNotFoundError:
            raise SystemError(self.urls + ' was not found.')

    @staticmethod
    def split_url(url):
        info = url.split(':::')
        if len(info) > 1:
            url = {'name': info[0], 'url': info[1]}
        else:
            url = {'name': '', 'url': info[0]}
        return url

    def parse_urls(self, urls_list):
        urls = []
        urls_found = []

        for url in urls_list:
            # remove '\n' from the string
            url = url.rstrip()

            # if it's a blank line it will append a new list
            if not url:
                urls.append(urls_found)
                urls_found = []
                continue

            urls_found.append(self.split_url(url))

        if len(urls_found) != 0:
            urls.append(urls_found)

        # just returns lists that are not empty
        urls = [list_not_empty for list_not_empty in urls if len(list_not_empty) > 0]

        return urls
