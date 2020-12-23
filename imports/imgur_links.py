from imgurpython import ImgurClient

def image_list(CLIENT_ID, CLIENT_SECRET):
    client = ImgurClient(CLIENT_ID, CLIENT_SECRET)
    images = client.gallery()
    images_list = []

    for image in images:
        images_list.append(image.link)

    return images_list