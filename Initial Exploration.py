#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 08:01:30 2019

@author: loganguerry
"""

# ==================================================== #
# ===== Working User Token Access to Discogs API ===== #
# ==================================================== #

#!pip install discogs_client
import discogs_client

# input personal user token (for exploration)
personal_token = ''

d = discogs_client.Client('BartsRecordShopExploration', user_token=personal_token)

# SAMPLE SEARCHES

# searching by release name
results = d.search('All Eyez On Me', type='release')
results.pages
artist = results[0].artists[0]
artist.name

# searching by artist ID
results = d.search('a1198658', type='artist')
artist = results[0]
artist.name
# OR
results[0].name

# pulling artists ID
artist = d.artist(2195284)
artist.releases.page(1)
