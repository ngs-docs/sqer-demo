#! /usr/bin/env python
import argparse
import screed
import sqer

def main():
   parser = argparse.ArgumentParser()
   parser.add_argument('filenames', nargs='+')

   args = parser.parse_args()

   total = 0
   for filename in args.filenames:
       records = screed.open(filename)
       for record in records:
          print len(record.sequence)

if __name__ == '__main__':
   main()
