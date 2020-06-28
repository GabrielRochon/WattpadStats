# WattpadStats
WattpadStats tracks your Wattpad story's stats using a web scraper. It helps you track your progress and the exposure of your novel on the platform. 

# How does it work?
Modify the URL of your novel in scraper.py (top of script). Once it's done, simply run the Python script. The script will web-scrape your page to gather informations about it (for non-cs students, web scraping is basically extraction of a web page's code). It then outputs this data into an Excel spreadsheet.

I cannot stress enough that setting up an automated task (if you're on Windows) that executes the script every day at a set time is extremely important, as you wouldn't get realistic data on a fixed 24-hour span without it.

# Versions
## Version 1.2
Additions:
- **Stats per chapters**: individual sheets are created for reads, votes and parts to show your chapters' individual growth in exposure!
  - This will give you a better idea of what your readers are reading particularily, instead of just general stats from the main worksheet.
Bug fixes:
- Corrected bug where thousands/millions views/reads would make the script crash. This is due to the fact that it would attempt to convert strings with Ks and Ms in it, then attempt to substract it.

## Version 1.1
Additions:
- **Increments from yesterday** are shown next to reads, votes and parts.
- The output is now an **Excel spreadsheet** instead of a regular text file. This makes the output cleaner.
- The script extracts your story's title all by itself. *Good boy!*

## Version 1.0
First version of the snippet. Currently extracts & stores in a text file:
- Readers count
- Viewers count
- Nb of parts

# Plans for future 
- Rankings
  - Although this would only work for the English version of Wattpad, as it is the basic language when accessing it via a fresh browser. This is problematic for people like me which publish stories in another language.
  
- Add styling to the spreadsheet. It's pretty boring right now!

- Look into a known bug where names with particular title with special characters would prevent creation of Excel file
  
- And more... feel free to message me your ideas => rochon.gabriel1@gmail.com
