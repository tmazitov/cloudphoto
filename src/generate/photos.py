
import src.photo.list as bucket
from src.settings import URL

class Args():
    def __init__(self, album):
        self.album = album

def page(album_name , doc, tag, text):
    photos_list = bucket.photos_list(Args(album_name))

    with tag('div', klass="galleria", id = f"album__{album_name}"):
        with tag('h1', klass="galleria__title"):
            text(album_name)
        
        with tag('div', klass="galleria__cont__current"):
            doc.stag('img', id=f"current__image__{album_name}", src=f'{URL}albums/{album_name}/{photos_list[0]}', height="inherit")

        with tag('div', klass="galleria__cont__items"):
            for photo in photos_list:
                with tag('div', klass="galleria_item"):
                    with tag('div', klass="bg-fon", onclick=f"selectPhoto('{photo}')"): 
                        text("")
                    doc.stag('img', src=f'{URL}albums/{album_name}/{photo}', height="148px")

        with tag('script'):
            text(f"var {album_name}_photos = {photos_list.__str__()}; ")
        
    result = doc.getvalue()
    return result.capitalize()