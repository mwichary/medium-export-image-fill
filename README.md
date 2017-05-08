# medium-export-image-fill

Medium allows you to download your story archive, but that archive doesn’t contain your images. Ergo, it is not really an archive.

This script:
- downloads all the images from your medium articles locally
- rewrites the archive files so that they point to the local images


### Instructions

1. Request your Medium archive from the bottom of https://medium.com/me/settings (Export content).

TK IMAGE


2. Wait for the email.
3. Download the archive from the email.
4. Unpack it somewhere.
5. Go to the root directory of that archive and run `medium-export-image-fill.py` there (using terminal/command line).

Note: You can interrupt the script at any time and run it again – it should start where it left off.

TK IMAGE
<img width="1154" src="https://cloud.githubusercontent.com/assets/2061609/21486338/edb3daf4-cb67-11e6-88ca-928b1b017b10.png">


### Details

- The script downloads the images in highest (original) quality.
- Images are downloaded into `images/` subdirectory.
- The original versions of modified archive files are saved in `original_articles/`, just in case.


### FAQ

**Does this work on Windows?**

Not sure. I wrote/tested it on Mac OS only. If you run it on Windows (successfully or not), please let me know.

**How about Linux?**

Some reported it worked for them properly on Ubuntu, FreeBSD, and Debian.


### License

This script is in public domain. Run free.


### Version history

**1.00 (8 May 2017)**
- Initial release
