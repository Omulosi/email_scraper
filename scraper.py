import os
import sys
import string
import re
from lxml.html import fromstring
import requests
from urllib.parse import urljoin, urlparse
from link_crawler import link_crawler
from threaded_crawler import threaded_crawler

def scraper(url, html):
    """
    Extracts data
    """

    if re.search(r'/filles/[a-zA-Z]+-?\d*/$', url):
        file_name = [word for word in url.split('/') if word][-1]
        is_invalid_name = [c for c in file_name if c in string.punctuation]
        if is_invalid_name:
            sys.exit(1)
        domain = '{}://{}'.format(urlparse(url).scheme, urlparse(url).netloc)
        dir_path = './data/{}'.format(file_name)

        tree = fromstring(html)
        pictures = tree.xpath('//div[@id="escort-pictures-gallery"]/a/img/@src')
        videos = tree.xpath('//video[contains(@class, "embed-responsive-item video-player")]/source/@src')
        if pictures or videos:
            os.makedirs(dir_path, exist_ok=True)

        if pictures:
            for pic_url in pictures:
                img_url = '{}{}'.format(domain, pic_url)
                img_name = img_url.rsplit('/', 1)[1]
                img_path = '{}/{}'.format(dir_path, img_name)

                # Download the image
                resp = requests.get(img_url, allow_redirects=True)
                with open(img_path, 'wb') as in_file:
                    in_file.write(resp.content)

        if videos:
            # Only download the first video
            video_url = videos[0]
            video_url = '{}{}'.format(domain, video_url)
            video_name = video_url.rsplit('/', 1)[1]
            video_path = '{}/{}'.format(dir_path, video_name)

            # Download the video
            resp = requests.get(video_url, stream=True)
            with open(video_path, 'wb') as in_file:
                for chunk in resp.iter_content(chunk_size=1024):
                    if chunk:
                        in_file.write(chunk)
                        in_file.flush()
        

        try:
            html_path = '{}/{}'.format(dir_path, file_name+'.html')
            with open(html_path, 'w') as f:
                f.write(html)

        except FileNotFoundError as err:
            print('Invalid file name #' + file_name +' : Skipping')

