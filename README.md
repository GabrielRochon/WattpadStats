# WattpadStats
WattpadStats tracks your Wattpad story's stats using a web scraper. It helps you track your progress and the exposure of your novel on the platform. 

# How does it work?
Modify the title & the URL of your novel in scraper.py. Once it's done, simply run the Python script. The script will web-scrape your page to gather informations about it (for non-cs students, web scraping is basically extraction of a web page's code). It then outputs this data into an Excel spreadsheet.

I cannot stress enough that setting up an automated task (if you're on Windows) that executes the script every day at a set time is extremely important, as you wouldn't get realistic data on a fixed 24-hour span without it.

# Versions
## Version 1.1 (June 27th 2020)
Additions:
- The output is now an Excel spreadsheet instead of a regular text file. This makes the output cleaner.

## Version 1.0 (June 27th 2020)
First version of the snippet. Currently extracts & stores in a text file:
- Readers count
- Viewers count
- Nb of parts

# Plans for future 
- Rankings
  - Although this would only work for the English version of Wattpad, as it is the basic language when accessing it via a fresh browser. This is problematic for people like me which publish stories in another language.
  
- Increase from yesterday
  - How many reads/viewers/parts/ranks(?) have I earned since the last time data was extracted?
