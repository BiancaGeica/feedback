#!/usr/bin/env python3

"""
Extract Moodle enrolled users as per-course JSON file.
"""

import sys
import pickle
import argparse
import moodlews


def main():
    """Extract Moodle enrolled users as per-course JSON file.
    Moodle configuration file and course Pickle file are provided
    as arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', nargs=1, required=True,
                        help='Configuration file')
    parser.add_argument('-l', '--courses', nargs=1, required=True,
                        help='Courses file in Pickle format')
    parser.add_argument('-d', '--dump', nargs=1, required=True,
                        help='Directory where to extract files')
    args = parser.parse_args()

    # Obtain Moodle credentials.
    moodlews.parse_config(args.config[0])
    moodlews.get_auth_token()
    moodlews.get_userid()

    # Retrieve courses from pickle file.
    courses = pickle.load(open(args.courses[0], "rb"))
    moodlews.extract_enrolled_users_for_courses(courses, args.dump[0])


if __name__ == "__main__":
    sys.exit(main())
