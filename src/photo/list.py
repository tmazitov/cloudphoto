from src.settings import S3_CLIENT, BUCKET_NAME


def photos_list(args):
    if args.album == None:
        assert "Error: album name is undefind"
        return

    prefix = "albums/" + args.album
    result = S3_CLIENT.list_objects(Bucket=BUCKET_NAME, Prefix=prefix)
    if "Contents" not in result:
        assert "Error: album with this name is undefind"
        return

    photos_path_list = []
    all_images = result["Contents"]
    for image in all_images:
        photos_path_list.append(image["Key"].replace(prefix + "/", ""))

    if photos_path_list.__len__() != 0:
        print(f"-- Photos list of '{args.album}' album:")
    for photo_name in photos_path_list:
        print(f"---- {photo_name}")

    return photos_path_list


def albums_list(args):
    prefix = "albums"
    result = S3_CLIENT.list_objects(Bucket=BUCKET_NAME, Prefix=prefix)
    if "Contents" not in result:
        assert "Error: albums is undefind"
        return

    albums_name_list = []
    all_albums = result["Contents"]
    for album in all_albums:
        album_path = album["Key"]
        album_path = album_path.replace(prefix + "/", "")
        album_name = album_path.split("/")[0]
        albums_name_list.append(album_name)

    albums_name_list = set(albums_name_list)
    if albums_name_list.__len__() != 0:
        print("-- Albums list:")
    for album_name in albums_name_list:
        print(f"---- {album_name}")

    return list(albums_name_list)
