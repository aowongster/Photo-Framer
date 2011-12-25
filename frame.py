#!/usr/bin/python
# File Name: frame.py
# Created:   23-12-2011

import sys
import os
import Image, ImageDraw

import argparse

def parse_opts():
  """ argparser """
  parser = argparse.ArgumentParser(description="Get opts for framer")
  parser.add_argument('-c', '--color', type=str, default='white',
  help="""color of frame
  PIL recognizes many html colors.
  for a full list: http://www.w3schools.com/html/html_colornames.asp
  default color is white.
  """)
  parser.add_argument('-f', '--file', required=True, help="input picture")
  parser.add_argument('-b', '--background', help="background image")

  return parser.parse_args()

# draw a border for my pictures!

# argparse for color!
def main(argv):
  """main func"""
  # match from sample image
  args = parse_opts()
  try:
    fname = args.file
    mainImg = Image.open( fname )
  except:
    print "Bad Input file"
    sys.exit(1)

  mw,mh = mainImg.size

  nw = int( mw * 1.2 )
  nh = int( mh * 1.2 )

  # need to customize this for variable colors
  if not args.background:
    im = Image.new("RGB", (nw, nh), args.color)
  else:
    try:
      im = Image.open( args.background )
      im = im.resize( (nw, nh) )
    except:
      print "Bad background file"
      sys.exit(1)

  # should be half of the change to center it!
  box = tuple( map(lambda x: int(x *.1), [mw, mh]))
  im.paste(mainImg, box)

  # change file name and copy image type?
  name, ext = os.path.splitext(fname)
  ext = ext[1:]           # remove period
  if ext.lower() == 'jpg': ext = 'jpeg'

  # appending f for frame
  im.save(name + 'F' + '.' + ext, ext)

if __name__ == "__main__":
  sys.exit(main(sys.argv))

