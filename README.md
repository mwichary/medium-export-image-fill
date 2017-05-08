# medium-export-image-fill

Medium allows you to download your story archive, but that archive doesn’t contain your images. Ergo, it is not really an archive.

This script:
- downloads all the images from your medium articles locally
- rewrites the archive files so that they point to the local images

(I wrote a [similar script for Twitter archive](https://github.com/mwichary/twitter-export-image-fill).)

### Instructions

1. Request your Medium archive from the bottom of https://medium.com/me/settings (Export content).

> <img width="735" alt="screen shot 2017-05-08 at 10 46 14" src="https://cloud.githubusercontent.com/assets/2061609/25822889/01e3f122-33ef-11e7-9eca-85ec5778fcc4.png">

2. Wait for the email.
3. Download the archive from the email.
4. Unpack it somewhere.
5. Go to the root directory of that archive and run `medium-export-image-fill.py` there (using terminal/command line).

Note: You can interrupt the script at any time and run it again – it should start where it left off.

<img width="1210" alt="screen shot 2017-05-08 at 10 38 14" src="https://cloud.githubusercontent.com/assets/2061609/25822878/f8c5f748-33ee-11e7-9694-afd688610025.png">

### Details

- The script downloads the images in highest quality. (Owing to how Medium image server works, those won’t be the exact original image files you uploaded, but they should be in the same resolution. This is particularly important for animated GIFs.)
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
