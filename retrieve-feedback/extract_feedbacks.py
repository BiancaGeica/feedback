#!/usr/bin/env python3

"""
Extract Moodle feedback contents as per-feedback JSON file.
"""

import sys
import pickle
import argparse
import moodlews


def main():
    """Extract Moodle feedback contents as per-feedback JSON file.
    Moodle configuration file and feedback metadata Pickle file are provided
    as arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', nargs=1, required=True,
                        help='Configuration file')
    parser.add_argument('-f', '--feedbacks', nargs=1, required=True,
                        help='Feedbacks file in Pickle format')
    args = parser.parse_args()

    # Obtain Moodle credentials.
    moodlews.parse_config(args.config[0])
    moodlews.get_auth_token()
    moodlews.get_userid()

    # Retrieve feedbacks from pickle file.
    feedbacks = pickle.load(open(args.feedbacks[0], "rb"))
    moodlews.extract_feedbacks(feedbacks)


if __name__ == "__main__":
    sys.exit(main())
