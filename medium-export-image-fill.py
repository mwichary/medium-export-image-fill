#!/usr/bin/env python

'''
Medium export image fill 1.00
by Marcin Wichary (aresluna.org)

Site: https://github.com/mwichary/medium-export-image-fill

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

For more information, please refer to <http://unlicense.org/>
'''

# Imports
# ---------------------------------

import argparse
import json
import os
import re
import stat
import string
import sys
import time
import urllib
from shutil import copyfile
# The location of urlretrieve changed modules in Python 3
if (sys.version_info > (3, 0)):
    from urllib.request import urlretrieve
else:
    from urllib import urlretrieve


# Main entry point
# ---------------------------------

# Introduce yourself

print("Medium export image fill 1.00")
print("by Marcin Wichary (aresluna.org) and others")
print("use --help to see options")
print("")

# Prepare variables etc.

image_count_global = 0
if not os.path.isdir("original_articles"):
  os.mkdir("original_articles")

# We need to impersonate a browser for downloads from CloudFlare to succeed
urllib.URLopener.version = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'

# Find all the articles to be processed

articles = []
for filename in os.listdir("."):
  if filename.endswith(".html"):
    articles.append(filename)

print("To process: %i article(s)..." % (len(articles)))
print("(You can cancel any time. Next time you run, the script should resume at the last point.)")
print("")

# Loop 1: Go through all the articles
# -----------------------------------

for article_count, article_filename in enumerate(articles):
  try:
    # Display progress
    count_string = '[%i/%i] ' % (article_count + 1, len(articles))
    print '%s%s...' % (count_string, article_filename)

    # Make a copy of the original file, just in case (only if it doesn't exist before)
    backup_filename = "original_articles/" + article_filename
    if not os.path.isfile(backup_filename):
      copyfile(article_filename, backup_filename)

    # Open file, find all images
    with open(article_filename, 'r') as file:
      article_contents = file.read()
    
    images = re.findall(r'(<img class="graf-image"(.*?)src="(.*?)">)', article_contents)

    # Loop 2: Go through all the images in an article
    # -----------------------------------------------

    for image_count, image in enumerate(images):
      
      # Create an article-specific directory to download images into
      directory_name = os.path.splitext(article_filename)[0]
      if (image_count == 0) and not os.path.isdir(directory_name):
        os.mkdir(directory_name)

      image_server_url = image[2]

      # Check the URL. If it starts with https://, it means we have to download the image.
      # If it doesn't, it means we already downloaded the image and rewrote the URL to point
      # to a local file
      skip_download = False
      if image_server_url[:8] != 'https://':
        skip_download = True

      # Get the image id, used to determine local filename
      image_id = re.findall(r'\/(([^\/]*?)\.([a-z]+))$', image_server_url)[0][0]

      # Update the user
      progress_string = "[%i/%i] %s %s..." %\
          (image_count + 1, len(images), "Skipping" if skip_download else "Downloading", image_id)
      progress_string = progress_string.rjust(len(progress_string) + len(count_string))
      sys.stdout.write("\r" + progress_string)
      sys.stdout.write("\033[K") # Clear the end of the line
      sys.stdout.flush()

      if not skip_download:
        # Rewrite the URL to get the maximum quality image from the server
        image_server_high_quality_url = re.sub(r'\/max\/[0-9]+\/', '/', image_server_url, 1)

        image_local_filename = directory_name + '/' + image_id

        # Download the file (try a few times if need be)
        downloaded = False
        download_tries = 3
        while not downloaded:
          try:
            urlretrieve(image_server_high_quality_url, image_local_filename)
          except:
            download_tries = download_tries - 1
            if download_tries == 0:
              print("")
              print("Failed to download %s after 3 tries." % better_url)
              print("Please try again later?")
              sys.exit()
            time.sleep(5) # Wait 5 seconds before retrying
          else:
            downloaded = True

        image_count_global = image_count_global + 1

        # Rewrite the URL to point to a local file, and re-save the article
        article_contents = re.sub(r'(<img class="graf-image"(.*?)src="{0}">)'.format(re.escape(image_server_url)), 
            r'<img class="graf-image"\2src="{0}">'.format(image_local_filename),
            article_contents, 1)
        with open(article_filename, 'w') as file:
          file.write(article_contents)

    # Remove the last downloaded file from the screen
    sys.stdout.write("\r")
    sys.stdout.write("\033[K") # Clear the end of the line
    sys.stdout.flush()

  except KeyboardInterrupt:
    print("")
    print("Interrupted! Come back any time.")
    sys.exit()

# End loop 1 (all the months)
print("")
print("Done!")
print("%i images downloaded in total." % image_count_global)
print("")
