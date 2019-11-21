import urllib.request
from requests import get

#Archive locations
url = 'https://www.asxhistoricaldata.com/data/2019jan-june.zip'


def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

download(url,"1.zip")

#wget the archive zip


# unzip to a folder


# recurse each file and import in postgres db
