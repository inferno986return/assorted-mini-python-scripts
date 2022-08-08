import qrcode

img = qrcode.make('https://frasers.group/')
type(img)  # qrcode.image.pil.PilImage
img.save("frasers_group.png")
