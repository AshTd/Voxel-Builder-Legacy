from app import VoxelBuilder


def main():
    """ Initializes and runs the VoxelBuilder application. """
    try:
        # Initialize the VoxelBuilder application
        app = VoxelBuilder()
        # Run the application
        app.run()
        print('Done!')

    except Exception as err:
        # Handling exceptions
        print(f'Error occured while running program:')
        print(f'{err}')
        exit(1)


if __name__ == '__main__':
    # Run the application
    print('Starting VoxelBuilder application...')
    main()
