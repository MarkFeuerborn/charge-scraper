UploadToDropbox = True
LatestFileName = 'latest.txt'

# Paths
PathToOutput = '/home/pi/Scraper/Output'
PathToDropbox = '/full/path/to/dropbox-uploader/script'

# Franklin County court web config
RootUrl = 'http://www.fcmcclerk.com/storage/shared/daily-arraignment/'
def GetIssuePageUrl(page):
    return '{}/issues?page={}'.format(RootUrl, page)

# The above needs configured to figure out how to pull the latest date rather than the latest issue number

def GetDownloadPageUrl(url):
    return '{}/{}'.format(RootUrl, url)
