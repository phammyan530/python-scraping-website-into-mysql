from tqdm import tqdm
import mysql.connector
import urllib.request

mydb  = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="_imdbtop2500"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM movies where img is not null")
myresult = mycursor.fetchall()

for row in tqdm(myresult):
    try:
        urllib.request.urlretrieve(row[8], "movie_posters/" + str(row[0]) + ".jpg")
    except:
        print('err at row id: ' + str(row[0]))