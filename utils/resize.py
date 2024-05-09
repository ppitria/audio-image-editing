from PIL import Image
import io

def image_resize(image_file):
    image = Image.open(image_file.stream)

    width, height = image.size

    resize_image = image.resize((width,height), resample=Image.Resampling.NEAREST)

    img_io = io.BytesIO()
    resize_image.save(img_io, compress_level=9, format='PNG')
    img_io.seek(0)

    return img_io