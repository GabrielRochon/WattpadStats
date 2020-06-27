# WattpadStats
WattpadStats tracks your Wattpad story's stats using a web scraper. It helps you track your progress and the exposure of your novel on the platform. 

# How does it work?
Modify the URL of your novel in scraper.py (lines 10 & 11). Once it's done, simply run the Python script. The script will web-scrape your page to gather informations about it (for non-cs students, web scraping is basically extraction of a web page's code). It then outputs this data into an Excel spreadsheet.

I cannot stress enough that setting up an automated task (if you're on Windows) that executes the script every day at a set time is extremely important, as you wouldn't get realistic data on a fixed 24-hour span without it.

# Versions
## Version 1.1 (June 27th 2020)
Additions:
- Increments from yesterday are shown next to reads, votes and parts.
- The output is now an Excel spreadsheet instead of a regular text file. This makes the output cleaner.
- The script extracts your story's title all by itself. *Good boy!*

## Version 1.0 (June 27th 2020)
First version of the snippet. Currently extracts & stores in a text file:
- Readers count
- Viewers count
- Nb of parts

# Plans for future 
- Rankings
  - Although this would only work for the English version of Wattpad, as it is the basic language when accessing it via a fresh browser. This is problematic for people like me which publish stories in another language.
  
- Handle "Ks" and "Ms" when gathering stats. Retrieving a story with 1000+ views/votes/parts will break the script (for now).
  
- And more... feel free to message me your ideas => rochon.gabriel1@gmail.com
