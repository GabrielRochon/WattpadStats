# Basic web scraper that collects views, votes & parts of your Wattpad story
# Ranks are language-dependant, so they wouldn't be scraped correctly
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from openpyxl import Workbook, load_workbook
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

# Slice those strings into numbers
reads = leaves[0][1:-6]                 # Removes last 6 chars: "100 Reads" - " Reads" = 100
votes = leaves[1][1:-6]                 # Removes last 6 chars: "100 Votes" - " Votes" = 100
parts = leaves[2][:-11]                 # Removes last 11 chars: "7 Part Story" - " Part Story" = 7

# Populate Excel file with numerical stats
filename = title + ' stats.xlsx'
existing_file = False
if(os.path.isfile(filename)):
    existing_file = True

row = 1
column = 1

if not existing_file:

    wb = Workbook()
    ws = wb.active
    header = [ "DATE", "READS", "VOTES", "PARTS" ]
    ws.append(header)
    row += 1
else:
    wb = load_workbook(filename=filename)
    ws = wb.active
    row = ws.max_row + 1

ws.column_dimensions['A'].width = 20      # Bigger row to display full date

today = datetime.today().strftime('%d/%m/%Y')

data = [ today, reads, votes, parts ]
for item in data:
    ws.cell(row, column, item)
    column += 1

wb.save(filename)
