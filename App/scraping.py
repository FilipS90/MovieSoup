from bs4 import BeautifulSoup
import importlib

def build(movieDetails, movie, movieName, channelName, genres=None):
    year = ''
    try:
        year = movieDetails.split(',')[1].strip()
    except:
        print(movieDetails)
    timeOfAiring = movie.find('em').text
    return movieName + ' ' +  year + ' - ' + timeOfAiring + ' - ' + channelName + ' - ' + genres

def search(input, option):
    results = ''
    channelsModule = importlib.import_module('Channels')
    for channel in channelsModule.channels:
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

            if movieDetails != None:
                    movieNameEng = movieDetails.split(',')[0]

            # by movie name
            if option == 1:
                if movieNameSrb != None:
                    if input in movieNameSrb.lower():
                        onlyOnce = not onlyOnce
                        return build(movieDetails, movie, movieNameSrb, channelName)
                
                if (input in movieNameEng.lower()) & onlyOnce:
                    return build(movieDetails, movie, movieNameEng, channelName)

            # by genres
            if option == 2:
                levelOneSearch = movie.find('span', class_='h')
                if levelOneSearch.find('span') != None:
                    genres = levelOneSearch.find('span').text
                    genres = genres.lower()
                if input.lower() in genres:
                    results += build(movieDetails, movie, movieNameEng, channelName, genres)+'\n'

    if results != '':
        return results
                    

def doSearchAll(input, option):
    result = ''
    if option == 1:
        for movie in input:
            if movie == '':
                continue
            val = search(movie, option)
            if val != None:
                result += val+'\n'
        return result[: len(result) - 2]

    if option == 2:
        for genre in input:
            val = search(genre, option)
            if val != None:
                    result += val+'\n'
        return result[: len(result) - 2]
