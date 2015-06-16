#!/usr/bin/env python
__version__ = "0.1.dev0"

import argparse
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def main(args=None):
  parser = argparse.ArgumentParser(description='Apply watermark to an image')
  parser.add_argument('image_file')
  parser.add_argument('watermark_text')
  parser.add_argument('--opacity', default='1.', type=float)
  parser.add_argument('--color-tuple', dest='color_tuple', default=(255, 255, 255))
  parser.add_argument('--margins', default=(0, 0))
  # parser.add_argument('--font-name', default='helvetica')
  parser.add_argument('--font-path', dest='font_path', default='/System/Library/Fonts/Keyboard.ttf')
  parser.add_argument('--font-size', default=100)
  args = parser.parse_args()

  assert 0 < args.opacity <= 1 

  # print(args.font_name)
  font = ImageFont.truetype(args.font_path, args.font_size)

  image = Image.open(args.image_file)
  text_layer = Image.new('RGBA', image.size, (0,0,0,0))
  text_draw = ImageDraw.Draw(text_layer)
  text_size = text_draw.textsize(args.watermark_text, font=font)
  text_pos = [image.size[i] / 2 - text_size[i] / 2 - args.margins[i] for i in (0, 1)]
  text_draw.text(text_pos, args.watermark_text, font=font, fill=args.color_tuple)
  new_image = Image.composite(text_layer, image, text_layer)
  assert args.opacity == 1.
  new_image.save(args.image_file + '-water.jpg')
