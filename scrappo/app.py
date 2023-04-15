import subprocess
import sys

from scrappo.processor import Processor
from scrappo.settings.manager import Manager


def main():
    print('program entrypoint')
    arguments = Manager().configure_arguments()

    validate_settings(arguments['Settings'])

    video = Processor(arguments['Settings'])
    video.process()

    if arguments['Settings'].shutdown.value:
        subprocess.run(["shutdown", "-s"])


def validate_settings(arguments):
    if not arguments.run.value:
        sys.exit()

    if arguments.shutdown.value:
        print('The computer will be shutdown when this program is done.\n')


if __name__ == '__main__':
    main()
