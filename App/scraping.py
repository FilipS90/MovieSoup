from bs4 import BeautifulSoup
import importlib

def buildAndPrint(movieDetails, movie, movieName, channelName):
    year = movieDetails.split(',')[1].strip()
    timeOfAiring = movie.find('em').text
    print(movieName + ' (' + year + ')' + ' биће приказан у ' + timeOfAiring + ' на програму ' +
    channelName )

def doSearch(keyword):
    channels = importlib.import_module('Channels')
    for channel in channels:
        soup = BeautifulSoup(channel, 'lxml')

        movies = soup.find('div', class_='overflow').find_all('li')
        channelName = soup.find('h1', class_='bigheader').text.split('-')[0]

        if channelName[5:7] == 'SC':
            channelName += 'I-FI'

        for movie in movies:

            movieNameSrb = movie.find('strong', class_='title').text
            movieDetails = movie.find('strong', class_='desc').text

            onlyOnce = True

            if keyword in movieNameSrb.lower():
                onlyOnce = not onlyOnce
                buildAndPrint(movieDetails, movie, movieNameSrb, channelName)

            movieNameEng = movieDetails.split(',')[0]
            
            if (keyword in movieNameEng.lower()) & onlyOnce:
                buildAndPrint(movieDetails, movie, movieNameEng, channelName)
