from PIL import Image
# from io import BytesIO

def starter_kit(author):
    starter_kit_img = Image.open('../images/input/starter_pack.png')
    # asset = user.avatar_url_as(size=128)
    # data = BytesIO(await asset.read())
    data = '../images/input/pfp128.png'
    pfp = Image.open(data)
    pfp = pfp.resize((200, 200))

    starter_kit_img.paste(pfp, (396, 198))
    # new_img_path = f'../images/output/{ user.name }_starter_kit.png'
    new_img_path = f'../images/output/{ author }_starter_kit.png'
    starter_kit_img.save(new_img_path)

    return 0
# await ctx.send(file=discord.File(new_img_path))

_ = starter_kit('sirat')