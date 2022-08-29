### Python scraping website into MySQL server

 - MySQL Connection to Python and Creating DB with Scraping Top 250 Movies Page on IMDB site https://www.imdb.com/chart/top
 - Scrap the page with BeautifulSoup and insert the data into Database
 - Create MySQL database and insert scraping data.

Using BeautifulSoup package to scrape top 250 movies and got the following:

 - Movie ID
 - Movie Title
 - Release Year
 - Run Time
 - Genre
 - Rating
 - Director and Actors
 - Votes
 - Gross
 - Poster Image

ER Diagram

<img src="https://github.com/phammyan530/python-scraping-website-into-mysql/blob/main/movie_posters/2022-table.jpg" width="500">

### Using Python to download images from mysql databse

- Using Python, connect to imdbtop250 database, read all poster images SRC and download it to local
- Finish: we have data and images about Top 250 Movies.

<img src="https://github.com/phammyan530/python-scraping-website-into-mysql/blob/main/movie_posters/posters.jpg">

### How to use

Type the command for install the packages used in this project:
```bash
$ pip install beautifulsoup4
$ pip install requests
$ pip install tqdm
$ pip install mysql-connector-python==8.0.29
```
Change your mysql connection at line 100 of scraping-website-by-python-into-mysql.py

- host="localhost"
- user="root"
- password=""
- database="_imdbtop2500"

Run this command to use:
```bash
$ python3 scraping-website-by-python-into-mysql.py
$ python3 download-images-from-mysql.py
```