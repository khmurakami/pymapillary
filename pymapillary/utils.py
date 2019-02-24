
#https://www.mapillary.com/developer/api-documentation/#retrieve-image-sources
def download_image_by_key(key, image_resolution=320):

    """
    Download a image by the key
    """

    if image_resolution == 320:
        url = "https://d1cuyjsrcm0gby.cloudfront.net" + "/" + key + "/thumb-320.jpg"
    elif image_resolution == 640:
        url = "https://d1cuyjsrcm0gby.cloudfront.net" + "/" + key + "/thumb-640.jpg"
    elif image_resolution == 1024:
        url = "https://d1cuyjsrcm0gby.cloudfront.net" + "/" + key + "/blah-1024.jpg"
    elif image_resolution == 2048:
        url = "https://d1cuyjsrcm0gby.cloudfront.net" + "/" + key + "/thumb-2048.jpg"

    filename = wget.download(url)
    return True
