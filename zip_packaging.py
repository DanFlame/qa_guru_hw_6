import os
import os.path as path
import zipfile


def all_into_one():
    current_dir = path.dirname(path.abspath(__file__))
    print('current dir = ', current_dir)
    resources_dir = path.join(current_dir, 'resources')
    print('resources dir =', resources_dir)
    tmp_dir = path.join(current_dir, 'tmp')
    files = os.listdir(resources_dir)
    zip_path = path.join(tmp_dir, 'my_archive.zip')

    with zipfile.ZipFile(zip_path, mode='w', compression=zipfile.ZIP_DEFLATED) as my_archive:
        for file in files:
            print(file)
            add_file = path.join(resources_dir, file)
            my_archive.write(add_file)


all_into_one()
