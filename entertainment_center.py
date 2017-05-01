#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import fresh_tomatoes
import media

"""
The media Class is the container of the movies' info.

The fresh_tomatoes Class takes charge of rendering pages basic on the given
movies' info.

Title, intro, cover jpg's URL and the trailer's URL should be given in order.
"""

toy_story = media.Movie(
    "Toy Story", "A Story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# print(toy_story.story)

finding_nemo = media.Movie(
    "Finding Nemo", "The story of the clownfish named Marlin",
    "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
    "https://www.youtube.com/watch?v=wZdpNglLbt8")

movies = [toy_story, finding_nemo]
fresh_tomatoes.open_movies_page(movies)
