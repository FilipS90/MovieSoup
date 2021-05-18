from bs4 import BeautifulSoup
import requests
import sys

# from mojtv.net
HBO = requests.get('https://mojtv.net/kanal/tv-program/366/hbo').text
HBO_2 = requests.get('https://mojtv.net/kanal/tv-program/367/hbo2').text
Cinemax = requests.get('https://mojtv.net/kanal/tv-program/368/cinemax').text
Cinemax_2 = requests.get('https://mojtv.net/kanal/tv-program/369/cinemax-2').text
Cinestar_Fantasy = requests.get('https://mojtv.net/kanal/tv-program/600/cinestar-fantasy').text
Cinestar_TV_Comedy = requests.get('https://mojtv.net/kanal/tv-program/665/cinestar-tv-comedy').text
Cinestar_TV = requests.get('https://mojtv.net/kanal/tv-program/371/cinestar-tv').text
Cinestar_Action_and_Thriller = requests.get('https://mojtv.net/kanal/tv-program/372/cinestar-action--thriller').text
Cinestar_Premiere_1 = requests.get('https://mojtv.net/kanal/tv-program/373/cinestar-premiere-1').text
Cinestar_Premiere_2 = requests.get('https://mojtv.net/kanal/tv-program/374/cinestar-premiere-2').text
TV_1000 = requests.get('https://mojtv.net/kanal/tv-program/378/tv-1000').text
Fox_Life = requests.get('https://mojtv.net/kanal/tv-program/396/fox-life').text
Fox_Crime = requests.get('https://mojtv.net/kanal/tv-program/397/fox-crime').text
Fox_Movies = requests.get('https://mojtv.net/kanal/tv-program/403/fox-movies').text
Fox = requests.get('https://mojtv.net/kanal/tv-program/404/fox').text
Pink_Premium = requests.get('https://mojtv.net/kanal/tv-program/415/pink-premium').text
Pink_Family = requests.get('https://mojtv.net/kanal/tv-program/416/pink-family').text
Pink_Film = requests.get('https://mojtv.net/kanal/tv-program/417/pink-film').text
Pink_Movies = requests.get('https://mojtv.net/kanal/tv-program/418/pink-movies').text
Pink_Romance = requests.get('https://mojtv.net/kanal/tv-program/419/pink-romance').text
Pink_Sci_Fi = requests.get('https://mojtv.net/kanal/tv-program/420/pink-scfi--fantasy').text
Pink_Action = requests.get('https://mojtv.net/kanal/tv-program/421/pink-action').text
Pink_Thriller = requests.get('https://mojtv.net/kanal/tv-program/422/pink-thriller').text
Pink_Crime_and_Mystery = requests.get('https://mojtv.net/kanal/tv-program/423/pink-crime--mystery').text
Pink_Comedy = requests.get('https://mojtv.net/kanal/tv-program/425/pink-comedy').text
Pink_Horror = requests.get('https://mojtv.net/kanal/tv-program/427/pink-horror').text
Pink_Western = requests.get('https://mojtv.net/kanal/tv-program/432/pink-western').text
Pink_Classic = requests.get('https://mojtv.net/kanal/tv-program/433/pink-classic').text
Pink_World_Cinema = requests.get('https://mojtv.net/kanal/tv-program/470/pink-world-cinema').text
Diva = requests.get('https://mojtv.net/kanal/tv-program/444/diva').text
AXN = requests.get('https://mojtv.net/kanal/tv-program/445/axn').text
SciFi = requests.get('https://mojtv.net/kanal/tv-program/452/scifi').text
Klasik_TV = requests.get('https://mojtv.net/kanal/tv-program/184/klasik-tv').text
AMC = requests.get('https://mojtv.net/kanal/tv-program/437/amc').text

channels = [HBO, HBO_2, Cinemax, Cinemax_2, Cinestar_Fantasy, Cinestar_TV_Comedy, Cinestar_TV,
Cinestar_Action_and_Thriller, Cinestar_Premiere_1, Cinestar_Premiere_2, TV_1000, Fox_Life, Fox_Crime,
Fox_Movies, Fox, Pink_Premium, Pink_Family, Pink_Film, Pink_Movies, Pink_Romance, Pink_Sci_Fi,
Pink_Action, Pink_Thriller, Pink_Crime_and_Mystery, Pink_Comedy, Pink_Horror, Pink_Western,
Pink_Classic, Pink_World_Cinema, Diva, AXN, SciFi, Klasik_TV, AMC]

def buildAndPrint(movieDetails, movie, movieName, channelName):
    year = movieDetails.split(',')[1].strip()
    timeOfAiring = movie.find('em').text
    print(movieName + ' (' + year + ')' + ' биће приказан у ' + timeOfAiring + ' на програму ' +
    channelName )

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

        if sys.argv[1].lower() in movieNameSrb.lower():
            onlyOnce = not onlyOnce
            buildAndPrint(movieDetails, movie, movieNameSrb, channelName)

        movieNameEng = movieDetails.split(',')[0]
        
        if (sys.argv[1].lower() in movieNameEng.lower()) & onlyOnce:
            buildAndPrint(movieDetails, movie, movieNameEng, channelName)
