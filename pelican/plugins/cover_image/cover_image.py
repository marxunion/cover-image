from pelican import signals, settings
import os
from glob import glob


def add_cover(content_object):
    # Get the directory from the file path
    dir_path = os.path.dirname(content_object.relative_source_path)

    # Define a list of image file extensions to search for
    image_extensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff']

    filename = content_object.settings.get('COVER_FILENAME', 'cover')
    cover = None

    # Search for 'cover' image files with any of the defined extensions
    for ext in image_extensions:
        search_path = os.path.join(dir_path, f'{filename}.{ext}')
        matching_files = glob(search_path)

        # If a matching file is found, return its path
        if matching_files:
            # Write the path to the cover file to the object metadata
            content_object.cover = '/' + matching_files[0]
            break


def register():
    signals.content_object_init.connect(add_cover)
