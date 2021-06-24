"""
 This project is protected by the following license
 --

  MIT License
  Copyright (c) 2021 http-samc
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
"""

import argparse
import os

import klembord

def cleanify(args):
    """Strips newlines, tabs from a file and copies it to the clipboard

    Args:
        args (Namespace): parsed CLI flags from argparse
    """
    with open(args.file, 'r') as f:
        fileText = f.read()

    cleanedText = fileText.replace('\n', '').replace('\t', '')

    if args.repQuotes: cleanedText = cleanedText.replace('"', "'") # Replacing quotes if needed

    klembord.set_text(cleanedText) # Adding final str to clipboard

def main():
    """Creates parser and calls cleanify with args
    """
    # Setting up parser
    parser = argparse.ArgumentParser(
        description="Copy a file's contents to your clipboard while removing newlines.")

    parser.add_argument('-file', "-f",
        type = os.path.abspath,
        help = "The file to read.")

    parser.add_argument("--repQuotes", "--rq",
        action="store_true",
        default=False,
        help="Replace double quotes with single ones (helps when storing HTML in .json files)")

    args = parser.parse_args()

    # Calling cleaner
    try:
        cleanify(args)
        print("Cleaned and copied to clipboard!")

    except Exception as e:
        print(f"Error cleaning: {e}")

if __name__ == "__main__":
    main()