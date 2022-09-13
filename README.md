# charge-scraper

# This is a work-in-progress adaptation of a simple scraper for a newsroom application. When finished, it will automatically run with a cronjob to pull down arrest report .pdf files from a local court's website, scan them for a list of charges of interest as keywords, and then send an email alert to the newsroom when it finds them. The program is lightweight enough to work on a simple Raspberry Pi 1 Model B running Raspbian, and could be applied to any number of websites holding data of interest to journalists.

# This has been built for Python 3x. The three core modules - scraper.py, pdftranslator.py and emailalert.py - are all now functional on their own when ran manually. I am currently in the process of creating a master script that runs all three and lets them utilize information each brings back.

Special thanks to my little brother, Nicholas Feuerborn, and Andy Long for their help and guidance on the code!
