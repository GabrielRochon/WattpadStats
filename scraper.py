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
url = 'https://www.wattpad.com/story/224182827-jour-apr%C3%A8s-jour'
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
chap_stats_list = list()
count = 1
# for chap_url in urls:
#     print('Reading chapter ' + str(count) + '...', end = ' ', flush = True)
#
#     # Get info
#     chap_req = Request('http://wattpad.com/' + chap_url, headers={'User-Agent': 'Mozilla/5.0'})     # So bots don't 403 you
#     chap_webpage = urlopen(chap_req).read()
#     chap_soup = BeautifulSoup(chap_webpage, 'html.parser')
#
#     chap_reads = chap_soup.findChild("span", {"class": "reads"})
#     chap_votes = chap_soup.findChild("span", {"class": "votes"})
#     chap_comments = chap_soup.findChild("span", {"class": "comments on-comments"}).findChild("a")
#
#     chap_stats = [int(chap_reads.contents[2]), int(chap_votes.contents[2]), int(chap_comments.contents[0])]
#
#     chap_stats_list.append(chap_stats)
#
#     delay = random.random()*3 + 2            # Random delay from 2 to 5 secs
#     time.sleep(delay)
#     print('[OK] After ' + str(round(delay,2)) + ' seconds.')
#     count += 1

# Dummy values to avoid constant scraping
chap_stats_list = [[75, 6, 0], [102, 9, 3], [64, 4, 5], [58, 4, 5], [53, 2, 12], [45, 3, 4], [43, 3, 4], [38, 3, 2], [51, 4, 8], [32, 3, 6], [39, 3, 6], [51, 3, 6], [30, 2, 5], [28, 3, 5], [49, 3, 8], [64, 3, 8], [85, 2, 6], [60, 2, 0], [41, 2, 0], [17, 1, 0]]

# print(chap_stats_list)

###############################################################################

# OUTPUT TO EXCEL FILE ########################################################
# Slice those strings into numbers
reads = slice_reads(leaves[0])
votes = slice_votes(leaves[1])
parts = slice_parts(leaves[2])

# Populate Excel file with numerical stats
filename = title + ' stats.xlsx'
existing_file = False
if(os.path.isfile(filename)):
    existing_file = True

row = 1
column = 1

inc_reads = 0
inc_votes = 0
inc_parts = 0

# FIRST WORKSHEET: GENERAL INFO
if not existing_file:
    wb = Workbook()
    ws = wb.active
    header = [ "DATE", "READS", "", "VOTES", "", "PARTS", "" ]
    ws.append(header)
    row += 1
else:
    wb = load_workbook(filename=filename)
    ws = wb.create_sheet('General')
    row = ws.max_row + 1

    # Increments from yesterday
    yesterday = ws[ws.max_row]
    inc_reads = int(reads) - int(yesterday[1].value)
    inc_votes = int(votes) - int(yesterday[3].value)
    inc_parts = int(parts) - int(yesterday[5].value)

# Sets column sizes
columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G']       # Pretty sure there's a better way to do it, but for now it's fine
widths = [20, 10, 5, 10, 5, 10, 5]
for (width, col) in zip(widths, columns):
    ws.column_dimensions[col].width = width

# Actual output
today = datetime.today().strftime('%d/%m/%Y')
data = [ today, reads, inc_reads, votes, inc_votes, parts, inc_parts ]

for item in data:
    if column == 3 or column == 5 or column == 7:
        if item == 0:
            ws.cell(row, column, '')        # If incr. is null, don't output it
        else:
            ws.cell(row, column, '(+' + str(item) + ')')
    else:
        if column == 2 or column == 4 or column == 6:
            ws.cell(row, column, int(item))
        else:
            ws.cell(row, column, item)
    column += 1


# SECOND WORKSHEET: READS PER CHAPTER
wb.create_sheet('Reads per chap')
ws = wb['Reads per chap']

row = 1
column = 1

for chap in chap_stats_list:
    ws.cell(row, column, chap[0])
    column += 1
    # print(chap[0])
row += 1
column = 0




wb.save(filename)
