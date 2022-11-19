media_types = {"html": "text/html", "js": "application/javascript", "ico": "image/x-icon", "css": "text/css"}


def get_media_type(resource: str) -> str:
    extension = resource.rsplit('.', 1)[-1]
    content_type = media_types[extension] if extension in media_types else None
    return content_type
