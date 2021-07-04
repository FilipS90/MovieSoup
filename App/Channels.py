import requests
import concurrent.futures

# from mojtv.net
urls = ['https://mojtv.net/kanal/tv-program/366/hbo',
        'https://mojtv.net/kanal/tv-program/367/hbo2',
        'https://mojtv.net/kanal/tv-program/368/cinemax',
        'https://mojtv.net/kanal/tv-program/369/cinemax-2',
        'https://mojtv.net/kanal/tv-program/600/cinestar-fantasy',
        'https://mojtv.net/kanal/tv-program/665/cinestar-tv-comedy',
        'https://mojtv.net/kanal/tv-program/371/cinestar-tv',
        'https://mojtv.net/kanal/tv-program/372/cinestar-action--thriller',
        'https://mojtv.net/kanal/tv-program/373/cinestar-premiere-1',
        'https://mojtv.net/kanal/tv-program/374/cinestar-premiere-2',
        'https://mojtv.net/kanal/tv-program/378/tv-1000',
        'https://mojtv.net/kanal/tv-program/396/fox-life',
        'https://mojtv.net/kanal/tv-program/397/fox-crime',
        'https://mojtv.net/kanal/tv-program/403/fox-movies',
        'https://mojtv.net/kanal/tv-program/404/fox',
        'https://mojtv.net/kanal/tv-program/415/pink-premium',
        'https://mojtv.net/kanal/tv-program/416/pink-family',
        'https://mojtv.net/kanal/tv-program/417/pink-film',
        'https://mojtv.net/kanal/tv-program/418/pink-movies',
        'https://mojtv.net/kanal/tv-program/419/pink-romance',
        'https://mojtv.net/kanal/tv-program/420/pink-scfi--fantasy',
        'https://mojtv.net/kanal/tv-program/421/pink-action',
        'https://mojtv.net/kanal/tv-program/422/pink-thriller',
        'https://mojtv.net/kanal/tv-program/423/pink-crime--mystery',
        'https://mojtv.net/kanal/tv-program/425/pink-comedy',
        'https://mojtv.net/kanal/tv-program/427/pink-horror',
        'https://mojtv.net/kanal/tv-program/432/pink-western',
        'https://mojtv.net/kanal/tv-program/433/pink-classic',
        'https://mojtv.net/kanal/tv-program/470/pink-world-cinema',
        'https://mojtv.net/kanal/tv-program/444/diva',
        'https://mojtv.net/kanal/tv-program/445/axn',
        'https://mojtv.net/kanal/tv-program/452/scifi',
        'https://mojtv.net/kanal/tv-program/184/klasik-tv',
        'https://mojtv.net/kanal/tv-program/437/amc'
        ]

def getRequest(url):
    return requests.get(url).text

def concurrentGetRequest():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        global urls
        executorResult = [executor.submit(getRequest, url) for url in urls]

        results = []
        for f in concurrent.futures.as_completed(executorResult):
            results.append(f.result())
    return results

channels = concurrentGetRequest()