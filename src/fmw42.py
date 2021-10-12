# fmw42
# https://stackoverflow.com/a/56910532/10440128
from wand.image import Image
from wand.display import display
from wand.version import QUANTUM_RANGE

with Image(filename='text.jpg') as img:
    with img.clone() as copied:
        with img.clone() as hcl:
            hcl.transform_colorspace('hcl')
            with hcl.channel_images['green'] as mask:
                mask.auto_threshold(method='otsu')
                copied.composite(mask, left=0, top=0, operator='copy_alpha')
                img.transform_colorspace('gray')
                img.negate()
                img.adaptive_threshold(width=20, height=20, offset=0.1*QUANTUM_RANGE)
                img.negate()
                img.composite(copied, left=0, top=0, operator='over')
                img.save(filename='text_process.jpg')
