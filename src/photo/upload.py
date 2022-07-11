from glob import glob
from src.settings import S3_CLIENT, BUCKET_NAME


def upload_photo(args):
    if args.album == None:
        assert "Error: album name is undefind"
        return

    if args.path == None:
        assert "Error: path of folder with photos is undefind"
        return

    print("-- Start upload photos")
    album_name = args.album
    path_to_folder_of_photos = args.path

    jpg_paths = glob(f"{path_to_folder_of_photos}/*.jpg")  # only .jpg files
    jpeg_paths = glob(f"{path_to_folder_of_photos}/*.jpeg")  # only .jpeg files
    paths = [*jpg_paths, *jpeg_paths]

    if paths.__len__() != 0:
        print(f'-- In folder "{path_to_folder_of_photos}" photos was found:')
    else:
        print(f"-- Folder has no images with .jpg, .jpeg format")
        return

    for file_path in paths:
        print(f"---- {file_path}")
        with open(file_path, "rb") as f:
            new_path = file_path.replace(
                path_to_folder_of_photos, f"albums/{album_name}/"
            )
            S3_CLIENT.upload_fileobj(f, BUCKET_NAME, new_path)
    print("-- Uploading completed successfully")
