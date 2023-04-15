import argparse

from margument.argument import Argument
from margument.arguments import Arguments


class Settings(Arguments):
    def __init__(self):
        self.urls = Argument(name='urls',
                             abbreviation_name='-u',
                             full_name='--urls',
                             help_message='A list of URLs of the videos to download or the path of a .txt file containing a list of URLs.',
                             metavar="",
                             default=[])

        self.output = Argument(name='output',
                               abbreviation_name='-o',
                               full_name='--output',
                               help_message='The output folder path in which the videos will be downloaded.',
                               metavar="",
                               default='')

        self.type = Argument(name='type',
                             abbreviation_name='-t',
                             full_name='--type',
                             help_message='The type of the videos to download. Choices are "movies" or "series". The difference between the two '
                                          'is that a series expects to have seasons and these will be separated in different folders. Default is '
                                          '"movies".',
                             metavar="",
                             choices=['movies', 'series'],
                             default='movies')

        self.shutdown = Argument(name='shutdown',
                                 abbreviation_name='',
                                 full_name='--shutdown',
                                 help_message='Enable/disable if computer will shutdown when the program has ended: (default is disabled)'
                                              'True: --shutdown | False: --no-shutdown',
                                 metavar="",
                                 default=False)

        self.run = Argument(name='run',
                            abbreviation_name='-r',
                            full_name='--run',
                            help_message='If specified, it will start the resizing process with configured settings.',
                            metavar="",
                            default=False)

    def add_arguments(self, args_parser):
        args_parser.add_argument(self.urls.abbreviation_name, self.urls.full_name,
                                 nargs='*',
                                 help=self.urls.help_message,
                                 default=argparse.SUPPRESS)

        args_parser.add_argument(self.output.abbreviation_name, self.output.full_name,
                                 type=str,
                                 help=self.output.help_message,
                                 default=argparse.SUPPRESS)

        args_parser.add_argument(self.type.abbreviation_name, self.type.full_name,
                                 type=str,
                                 help=self.type.help_message,
                                 default=argparse.SUPPRESS)

        args_parser.add_argument(self.shutdown.full_name,
                                 action=argparse.BooleanOptionalAction,
                                 help=self.shutdown.help_message,
                                 default=argparse.SUPPRESS)

        args_parser.add_argument(self.run.abbreviation_name, self.run.full_name,
                                 action='store_true',
                                 help=self.run.help_message,
                                 default=argparse.SUPPRESS)

    def process_arguments(self, settings):
        # todo validate output path
        pass
