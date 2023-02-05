import os
import os.path as path
import zipfile


def all_into_one():
    current_dir = path.dirname(path.abspath(__file__))
    resources_dir = path.join(current_dir, 'resources')
    files = os.listdir(resources_dir)
    zip_path = path.join(resources_dir, 'my_archive.zip')

    with zipfile.ZipFile(zip_path, mode='w', compression=zipfile.ZIP_DEFLATED) as my_archive:
        for file in files:
            add_file = path.join(resources_dir, file)
            my_archive.write(add_file)

