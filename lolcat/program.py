import os
import subprocess

import cat_service


def main():
    # print header
    header()

    # create folders
    folder_path = create_folder()
    print(folder_path)

    # download cat images and save it in folder
    download_cats(folder_path)

    # display cats
    display(folder_path)

def header():
    print('-----------------------------------')
    print('          lol cat images')
    print('-----------------------------------')


def create_folder():
    folder = 'catpictures'
    fullpath = os.path.abspath(os.path.join(folder))
    print(fullpath)
    if not os.path.exists(fullpath):
        print("creating new directory.......")
        os.mkdir(fullpath)
    return fullpath


def download_cats(folder):
    cat_count = 8
    print("contacting server........")
    for i in range(1, cat_count+1):
        filename = f"cat{i}.jpg"
        cat_service.get_cat(folder, filename)
        print(f"Downloading image {i}.......")


def display(folder):
    subprocess.call(['explorer', folder])


if __name__ == '__main__':
    main()
