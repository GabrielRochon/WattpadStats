# Basic web scraper that collects views, votes & parts of your Wattpad story
# Ranks are language-dependant, so they wouldn't be scraped correctly
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from datetime import datetime
import os

# ENTER YOUR STORY INFO HERE ##################################################
url = 'https://www.wattpad.com/story/226573279-virtuel'
title = 'VIRTUEL'
###############################################################################

# Extract stats from your story page's HTML
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})     # So bots don't 403 you
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
stats = soup.findChild("div", {"class": "meta"})

leaves = list()
for i in stats.children:
    if(i != '\n'):
        leaves.append(i.contents[0])

# Slice those strings into numbers (careful, slicing will fail for non-English pages)
reads = leaves[0][1:-6]
votes = leaves[1][1:-6]
parts = leaves[2][:-11]

# Populate text file with numerical stats
filename = title + ' stats.txt'
existing_file = False
if(os.path.isfile(filename)):
    existing_file = True

f = open(filename, "a")
if existing_file == False:
    f.write('------------- --------- --------- ---------\n')
    f.write('DATE          READS     VOTES     PARTS    \n')
    f.write('------------- --------- --------- ---------\n')

today = datetime.today().strftime('%d/%m/%Y')

f.write(today + ' '*(14-len(today)))
f.write(reads + ' '*(10-len(reads)))
f.write(votes + ' '*(10-len(votes)))
f.write(parts + '\n')
f.close()
