from yattag import Doc, indent
from src.settings import URL
import  src.generate.photos as photos

album_page_styles = {
    'text' : {
        'main': open('./web/css/index.css', 'r').read(),
        'item': open('./web/css/album_item.css', 'r').read(),
    }
}

photo_page_styles = {
    'text' : {
        'main': open('./web/css/index.css', 'r').read(),
        'galleria': open('./web/css/galleria.css', 'r').read()
    }
}

def page(album_list):
    doc, tag, text = Doc().tagtext()
    if album_list is None:
        return ""

    with tag('html'):
        with tag('head'):
            with tag('style'):
                text(photo_page_styles['text']['main'])
                text(photo_page_styles["text"]["galleria"])
                text(album_page_styles["text"]["main"])
                text(album_page_styles["text"]["item"])

        with tag('body'):
            
            with tag('h1'):
                text('Альбомы')
            for album_name in album_list:
                with tag('div', klass="album__item", onclick=f"selectAlbum('{album_name}')"):
                    with tag('a'):
                        text(album_name)
            with tag('div', klass="info__cont"):
                for album_name in album_list:
                    photos.page(album_name, doc, tag, text)
            with tag('script'):
                text("""
                    var currentAlbum

                    function selectAlbum(albumName){
                        if(currentAlbum){
                            document.getElementById("album__" + currentAlbum).style.display = "none";
                        } else if (currentAlbum != albumName){
                            document.getElementById("album__" + albumName).style.display = "none";
                            currentAlbum = albumName;
                            return
                        } 
                        currentAlbum = albumName;
                        document.getElementById("album__" + albumName).style.display = "block";
                    }

                    function selectPhoto(photoName){
                        let currentImage = document.getElementById("current__image__"+ currentAlbum)
                        currentImage.src = '""" + URL + """' + 'albums/' + currentAlbum + '/' +photoName
                    }

                    """)
    result = doc.getvalue()
    return indent(result)