import os

from src.settings import S3_CLIENT, BUCKET_NAME

from .list import photos_list


def download_photo(args):
    if args.album == None:
        assert "Error: album name is undefind"
        return

    if args.path == None:
        assert "Error: path of folder for photos is undefind"
        return

    new_folder_path = args.path
    if not os.path.isdir(new_folder_path):
        assert "Error: path of folder for photos is invalid"
        return

    photos_path_list = photos_list(args)

    print(f"-- Start download photos from '{args.album}' album")
    for path in photos_path_list:

        bucket_path = f"albums/{args.album}/" + path
        local_path = args.path + "/" + path

        S3_CLIENT.download_file(BUCKET_NAME, bucket_path, local_path)

        print(f"---- {path} : success")

    print("-- Download completed successfully")
