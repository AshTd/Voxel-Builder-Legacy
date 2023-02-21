from app import VoxelBuilder

from os.path import expanduser
from logging import basicConfig, INFO, info, error
basicConfig(level=INFO, format='%(message)s')


def main():
    """ Initializes and runs the VoxelBuilder application """
    try:
        app = VoxelBuilder()
        app.run(f'{expanduser("~")}\\Desktop')
        info('Done!')

    except Exception as err:
        # Handling exceptions
        error(f'Error occured while running program:')
        error(f'{err}')
        exit(1)


if __name__ == '__main__':
    info('Starting VoxelBuilder application')
    main()
