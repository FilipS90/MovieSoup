from bs4 import BeautifulSoup
import importlib

def build(movieDetails, timeOfAiring, movieName, channelName, genres=''):
    year = ''
    try:
        year = movieDetails.split(',')[1].strip()
    except:
        print('No year error')
    return movieName + ' ' +  year + ' - ' + timeOfAiring + ' - ' + channelName + genres

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
            
            timeOfAiring = movie.find('em').text
            movieNameSrb = movie.find('strong', class_='title')
            movieDetails = movie.find('strong', class_='desc')

            if movieNameSrb != None:
                movieNameSrb = movie.find('strong', class_='title').text

            if movieDetails != None:
                movieDetails = movie.find('strong', class_='desc').text

            onlyOnce = True

            if movieDetails != None:
                    movieNameEng = movieDetails.split(',')[0]

            if 'Telop sponzorski za film' in movieNameEng:
                continue

            # by movie name
            if option == 1:
                if movieNameSrb != None:
                    if input in movieNameSrb.lower():
                        onlyOnce = not onlyOnce
                        return build(movieDetails, timeOfAiring, movieNameSrb, channelName)
                
                if (input in movieNameEng.lower()) & onlyOnce:
                    return build(movieDetails, timeOfAiring, movieNameEng, channelName)

            # by genres
            if option == 2:
                levelOneSearch = movie.find('span', class_='h')
                if levelOneSearch.find('span') != None:
                    genres = levelOneSearch.find('span').text
                if input.lower() in genres.lower():
                    if '/' in movieNameEng:
                        movieNameEng = movieNameEng.split('/')[1]
                    results += build(movieDetails, timeOfAiring, movieNameEng, channelName, ' - ' + genres)+'\n'

    if results != '':
        return results.split('\n')
                    

def doSearchAll(input, option):
    if option == 1:
        result = ''
        for movie in input:
            if movie == '':
                continue
            val = search(movie, option)
            if val != None:
                result += val+'\n'
        return result[: len(result) - 2]

    if option == 2:
        result = []
        for genre in input:
            val = search(genre, option)
            if val != None:
                    result.extend(val)
        result.remove('')
        return result
