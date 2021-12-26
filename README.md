Runs on Python 3.9.5

A little app I made for myself using a Python library Beautiful Soup for HTML parsing and Tkinter for UI. Since I like catching my movies on TV, I was bored with going over TV guide every time I wanted to see some movie, so I just wanted to check if there was something which is currently on my watch list airing in the evening with a few clicks, as well as by some other parameters, such as genre or a year a movie was produced in. 

UI is in Serbian as channels targeted are Serbian.

Search options available are as follows:

- By movie name (doesn't have to be exact, can pick movies with certain keyword). These keywords are saved to X:\Users\currentUser\MovieSoupSearch.txt in Windows, not sure where in Linux, but I know IO operation supports Linux as well. Keywords can be removed from the list by double clicking them. The list is scrollable;
- By genre (relying on site for accuracy);
- By year the movie is produced (two fields, from and to).

Results list is scrollable. Double clicking any of results will do a google search with movie name and year as parameters, to easily check on imdb rating.

In case you want to check Претражи is the Search button.
