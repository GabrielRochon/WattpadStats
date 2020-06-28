# Basic web scraper that collects views, votes & parts of your Wattpad story
# Libraries
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from openpyxl import Workbook, load_workbook
from datetime import datetime
import os
import random
import time

# Source files
from slicing import *

# ENTER YOUR STORY INFO HERE ##################################################
url = 'https://www.wattpad.com/story/226573279-virtuel'
###############################################################################

# MAIN PAGE ###################################################################
# Extract stats from your story page's HTML
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})     # So bots don't 403 you
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
stats = soup.findChild("div", {"class": "meta"})

leaves = list()
for i in stats.children:
    if(i != '\n'):
        if(len(leaves) < 2):
            leaves.append(i['title'])
        else:
            leaves.append(i.contents[0])

title_wrapper = soup.findChild("div", {"class": "container"})
title = title_wrapper.findChild("h1").contents[0][:-1]
###############################################################################

# EVERY CHAPTER ###############################################################
# Get every chapter's URL and grab individual stats for each one of them
urls = list()
chapters = soup.find("ul", {"class": "table-of-contents"})
chapters_list = chapters.findAll("a")
for i in chapters_list:
    urls.append(i['href'])

# for item in urls:
#     print(item)

# Access every url to retrieve individual chapter stats
# WARNING: Gotta be careful with this, as Wattpad may see this as a potential DDoS
#   This process will take some time to ensure Wattpad doesn't blacklist our IP address
#   while accessing all of the stories' urls
count = 1
for url in urls:
    print('Reading chapter ' + str(count) + '...', end = ' ', flush = True)

    # Get info...

    delay = random.random()*3 + 2            # Random delay from 2 to 5 secs
    time.sleep(delay)
    print('[OK] After ' + str(round(delay,2)) + ' seconds.')
    count += 1

###############################################################################

# OUTPUT TO EXCEL FILE ########################################################
# Slice those strings into numbers
# reads = slice_reads(leaves[0])
# votes = slice_votes(leaves[1])
# parts = slice_parts(leaves[2])
#
# # Populate Excel file with numerical stats
# filename = title + ' stats.xlsx'
# existing_file = False
# if(os.path.isfile(filename)):
#     existing_file = True
#
# row = 1
# column = 1
#
# inc_reads = 0
# inc_votes = 0
# inc_parts = 0
#
# if not existing_file:
#     wb = Workbook()
#     ws = wb.active
#     header = [ "DATE", "READS", "", "VOTES", "", "PARTS", "" ]
#     ws.append(header)
#     row += 1
# else:
#     wb = load_workbook(filename=filename)
#     ws = wb.active
#     row = ws.max_row + 1
#
#     # Increments from yesterday
#     yesterday = ws[ws.max_row]
#     inc_reads = int(reads) - int(yesterday[1].value)
#     inc_votes = int(votes) - int(yesterday[3].value)
#     inc_parts = int(parts) - int(yesterday[5].value)
#
# # Sets column sizes
# columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G']       # Pretty sure there's a better way to do it, but for now it's fine
# widths = [20, 10, 5, 10, 5, 10, 5]
# for (width, col) in zip(widths, columns):
#     ws.column_dimensions[col].width = width
#
# # Actual output
# today = datetime.today().strftime('%d/%m/%Y')
# data = [ today, reads, inc_reads, votes, inc_votes, parts, inc_parts ]
#
# for item in data:
#     if column == 3 or column == 5 or column == 7:
#         if item == 0:
#             ws.cell(row, column, '')        # If incr. is null, don't output it
#         else:
#             ws.cell(row, column, '(+' + str(item) + ')')
#     else:
#         if column == 2 or column == 4 or column == 6:
#             ws.cell(row, column, int(item))
#         else:
#             ws.cell(row, column, item)
#     column += 1
#
# wb.save(filename)
