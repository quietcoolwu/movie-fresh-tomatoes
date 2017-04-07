#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import webbrowser


class Movie(object):
    """This class provides a way to store movies."""
    VALID_RATINGS = ("G", "PG", "PG-13", "R")

    def __init__(self, title, story, poster, trailer):
        self.title = title
        self.story = story
        self.poster = poster
        self.trailer = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
