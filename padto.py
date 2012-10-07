#!/usr/bin/python
import struct
import shutil
import os
import sys

def usage():
  print '''
  padto.py <input file> <padto size> <pattern> <output file name>
  '''
def main():
  # Read params:1. Filename, 2 Size, 3 pattern, 4 Output name
  # Input check
  if len(sys.argv) != 5:
    usage()
    sys.exit()
  src = sys.argv[1]
  padto = eval(sys.argv[2])
  patt = int(sys.argv[3], 10)
  dst = sys.argv[4]
  
  # Src file does not exist
  if not (os.path.isfile(src)):
    print "Input file not found"
    sys.exit()
  # Size is smaller than src file
  src_size = os.path.getsize(src);
  if padto <= src_size:
    print "Padto size {0} is smaller than input file size {1}"\
        .format(padto, src_size)
    sys.exit()
  
  if (os.path.isfile(dst)):
    os.remove(dst)
  
  print '''
  Source file: {0}
  Input file size:{1:d} bytes
  Pad to size: {2:d} bytes
  Pattern: {3}
  Output file: {4}
  '''.format(src, src_size, padto, patt, dst)
  
  # Save input as output file
  shutil.copyfile(src, dst)
  
  # Open output file
  f = open(dst, 'ab')
  
  # Loop append output file
  for i in range(src_size, padto):
    f.write(struct.pack('c', chr(patt)))
  
  # Close output file
  f.close
  print "Finished"
  sys.exit()

if __name__ == '__main__':
  main()
