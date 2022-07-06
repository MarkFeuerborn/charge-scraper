import config
import helpers
import scraper
import logging

## setup logging
logging.basicConfig(handlers=[logging.FileHandler('scraper.log'),logging.StreamHandler()], format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logging.info("Let's do some mad scraping")
latestIssueNo = helpers.RetrieveLatest(config.LatestFileName)
#print(f"Most recently downloaded issue is {latestIssue}")
logging.info("Most recently downloaded issue is {}".format(latestIssueNo))

pageCount = scraper.FindPageCount()
logging.info("There are {} pages...".format(pageCount))

logging.info("Looking for new issues...")
scraper.FindIssues(pageCount, latestIssueNo)
logging.info("Finished!")
