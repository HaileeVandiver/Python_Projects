import sqlite3 
conn = sqlite3.connect('database1.db')#create database and open connection
with conn:#while database connection is open
    cur = conn.cursor() #use cur to navigate 
   #create table called files
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT, col_filename TEXT)")
    conn.commit() #save changes to database
conn.close() #close the connection so no leakage

conn = sqlite3.connect('database1.db')
#list of file names
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
#loop through each object to find the filenames that end in .txt
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_filename) VALUES (?)", (x,))
            print(x)
conn.close()
    





