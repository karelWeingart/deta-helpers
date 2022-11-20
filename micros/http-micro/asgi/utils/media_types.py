"""module for file extensions vs mime types"""
media_types = {"html": "text/html",
               "js": "application/javascript",
               "ico": "image/x-icon",
               "css": "text/css"}


def get_media_type(resource: str) -> str:
    """returns mime type based on file extension"""
    extension = resource.rsplit('.', 1)[-1]
    content_type = media_types[extension] if extension in media_types else "text/html"
    return content_type
