from bs4 import BeautifulSoup
import importlib

def buildAndPrint(movieDetails, movie, movieName, channelName):
    year = movieDetails.split(',')[1].strip()
    timeOfAiring = movie.find('em').text
    return movieName + ' (' + year + ')' + ' - ' + timeOfAiring + ' - ' + channelName 

def search(keyword):
    channels = importlib.import_module('Channels')
    for channel in channels.channels:
        soup = BeautifulSoup(channel, 'lxml')

        movies = soup.find('div', class_='overflow').find_all('li')
        channelName = soup.find('h1', class_='bigheader').text.split('-')[0]

        if channelName[5:7] == 'SC':
            channelName += 'I-FI'

        for movie in movies:

            movieNameSrb = movie.find('strong', class_='title')
            movieDetails = movie.find('strong', class_='desc')

            if movieNameSrb != None:
                movieNameSrb = movie.find('strong', class_='title').text

            if movieDetails != None:
                movieDetails = movie.find('strong', class_='desc').text

            onlyOnce = True

            if movieNameSrb != None:
                if keyword in movieNameSrb.lower():
                    onlyOnce = not onlyOnce
                    return buildAndPrint(movieDetails, movie, movieNameSrb, channelName)
            
            if movieDetails != None:
                movieNameEng = movieDetails.split(',')[0]
                if (keyword in movieNameEng.lower()) & onlyOnce:
                    return buildAndPrint(movieDetails, movie, movieNameEng, channelName)

def doSearch_All(movies):
    result = ''
    for movie in movies:
        if movie == '':
            continue
        val = search(movie)
        if val != None:
            result += val+'\n'

    return result[: len(result) - 2]
