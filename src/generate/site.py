import src.photo.list as bucket
import src.generate.albums as albums
import src.generate.photos as photos

from src.settings import BUCKET_NAME, S3_CLIENT

def site(args):
    
    album_list = bucket.albums_list(args)

    page = albums.page(album_list)
    with open("./web/album_page.html",'w+') as file:
        file.write(page)
    
    website_configs = {
        'ErrorDocument': {'Key': 'error.html'},
        'IndexDocument': {'Suffix': 'album_page.html'},
    }

    S3_CLIENT.put_bucket_website(
        Bucket=BUCKET_NAME,
        WebsiteConfiguration=website_configs
    )

    with open('web/album_page.html', 'rb') as file:
        S3_CLIENT.upload_fileobj(file, BUCKET_NAME, file.name.split('/')[1])



