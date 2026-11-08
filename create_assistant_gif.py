from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

out = Path("www/assets/thaara_core.gif")
out.parent.mkdir(parents=True, exist_ok=True)
frames = []
for i in range(12):
    pulse = 10 + int(8 * (1 + __import__('math').sin(i / 12 * 2 * __import__('math').pi)))
    img = Image.new("RGB", (480, 480), (5, 8, 18))
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((90-pulse, 90-pulse, 390+pulse, 390+pulse), fill=(220, 20, 32, 55))
    glow = glow.filter(ImageFilter.GaussianBlur(24))
    img = Image.alpha_composite(img.convert("RGBA"), glow)
    d = ImageDraw.Draw(img)
    d.ellipse((110, 110, 370, 370), outline=(145, 18, 32), width=7)
    d.ellipse((128, 128, 352, 352), outline=(250, 50, 45), width=3)
    d.polygon([(155, 225), (220, 185), (260, 185), (325, 225), (260, 265), (220, 265)], outline=(255, 80, 65), fill=(70, 5, 12))
    eye = 18 + int(7 * (1 + __import__('math').sin(i / 12 * 2 * __import__('math').pi)))
    d.ellipse((214-eye, 225-eye, 214+eye, 225+eye), fill=(255, 220, 180))
    d.ellipse((266-eye, 225-eye, 266+eye, 225+eye), fill=(255, 220, 180))
    d.arc((180, 275, 300, 335), 10, 170, fill=(245, 45, 45), width=5)
    frames.append(img.convert("P", palette=Image.Palette.ADAPTIVE))
frames[0].save(out, save_all=True, append_images=frames[1:], duration=90, loop=0, optimize=True)
print(out)
