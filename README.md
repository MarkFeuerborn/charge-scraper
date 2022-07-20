# charge-scraper

# This is a work-in-progress adaptation of existing MagPi scrapers for a newsroom application. Its endgoal implementation is to pull down .pdf files from a court website, scan them for a list of charges of interest as keywords, and then send an email alert to the newsroom when it finds them. The project is still in its early stage, but is lightweight enough to work on a simple Raspberry Pi 1 Model B running Raspbian, and could be applied to any number of websites holding data of interest to journalists.

# This has been built for Python 3x

# So far, I have successfully gotten scraper.py and emailalert.py up and running.

# scraper.py downloads all of the .pdfs marked "4D" (could expand this to include "4C" with the right and/or in my if line).

#I need to work on this line
#if ('.pdf' and('4D')) in url:
#                                download_file('http://fcmcclerk.com' + url)

# emailalert.py so far, has been set up and tested to successfully send an email. Every time it runs the script, it sends an email saying "This is a delicious slice of Raspberry Pi," but that messaging will be changed to say "I found these charges: [keywords from pdf scraping]"

# I see this as about half of the work completed. Next steps:

# I need to build a script to look in the downloaded PDFs in my Output folder, and check the new ones for the keywords that we want to look for.

# Once all three scripts are done, I need to bring them all together into main.py - This would be the script that first runs scraper.py, then pdftranslator.py, and then finally emailalert.py.
