# Cloudphoto
>CLI application for photo storage into the Yandex Cloud Bucket. Based on boto3 (AWS SDK adaptation for Python).

## Installation:

1. Install dependencies:
    🔶[boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - main package for conect to Yandex Cloud Bucket
    🔶[dotenv](https://pypi.org/project/python-dotenv/) - workig with.env files 
    🔶[yattag](https://www.yattag.org/) - generate .html files in python
    
    🔷 Python 3.8 or higher
    🔷 Ubuntu or wsl

1. Setup configs to .config/cloudphoto/```cloudphotorc```: 

        [default]
        bucket=backet_nameaws_access_key_id=AK*****************LE
        aws_secret_access_key=wJ**********************************EY
        region=ru-central1
        endpoint_url=https://storage.yandexcloud.net

3. Setup yc ([Yandex Cloud]("https://cloud.yandex.ru/docs/cli/quickstart")) and [rclone](https://rclone.org/)

4. Using!

## Commands:
+ ```upload``` folder with photos to the Yandex Cloud Bucket.  
    * ```--path```  string  | path to the folder with photos for upload 
    * ```--album``` string  | your album name
    * ❗ uploading takes place in the root folder "albums"
    * ❗ valid image file extension is .jpg and .jpeg
    ---
+ ```download``` album with photos from the Yandex Cloud Bucket.```
    * ```--path```  string  | path to the folder for photos 
    * ```--album``` string  | album name
    ---
+ ```list-albums``` print a list of the saved albums```
+ ```list-photos``` print a list of thea saved photos by the album name```
    * ```--album``` string  | album name
    ---
+ ```generate-site``` is a command, which build .html files for to view photos in the user interface by YC Bucket  [Static website](https://cloud.yandex.ru/docs/tutorials/web/static) .

## Usefull:
Upload file changes to the YC Bucket
```bush
    rclone -v -P copy ~/cloudphoto/web yc:BUCKET-NAME
``` 
