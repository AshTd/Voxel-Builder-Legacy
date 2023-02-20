from app import VoxelBuilder

from logging import basicConfig, INFO, info, error
basicConfig(level=INFO, format='%(message)s')


def main():
    """ Initializes and runs the VoxelBuilder application """
    try:
        # Initialize the VoxelBuilder application
        app = VoxelBuilder()
        # Run the application
        app.run()
        info('Done!')

    except Exception as err:
        # Handling exceptions
        error(f'Error occured while running program:')
        error(f'{err}')
        exit(1)


if __name__ == '__main__':
    # Run the application
    info('Starting VoxelBuilder application...')
    main()
