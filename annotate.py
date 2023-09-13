#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""\
This tool performs content analysis on a given audio file and outputs the
results to a JSON file.

Usage: annotate.py INPUT_FILE OUTPUT_FILE
"""

from docopt import docopt
import librosa
import json

def content_analysis(audio, sample_rate):
    return {}

def main():
    args = docopt(__doc__, version='0.1.0')
    input_file = args['INPUT_FILE']
    output_file = args['OUTPUT_FILE']

    # Load the audio file
    audio, sample_rate = librosa.load(input_file)

    # Perform content analysis
    annotations = content_analysis(audio, sample_rate)

    # Write the annotations to a JSON file
    with open(output_file, 'w') as f:
        json.dump(annotations, f, indent=2)

if __name__ == '__main__':
    main()