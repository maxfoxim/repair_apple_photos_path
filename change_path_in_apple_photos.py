

import sqlite3

INPUT_FOLDER="Users/stephan/Desktop/2023/"
OUTPUT_FOLDER="Volumes/SDBilder/2023/"
FOLDER_DB_PHOTOS="/Users/stephan/Pictures/DresdenLibary.photoslibrary/database/Photos.sqlite"
#FOLDER_DB_PHOTOS="Photos.sqlite"

conn = sqlite3.connect(FOLDER_DB_PHOTOS)
cur = conn.cursor()

cur.execute("SELECT ZPATHRELATIVETOVOLUME FROM ZFILESYSTEMBOOKMARK where ZPATHRELATIVETOVOLUME LIKE ?;" , ("%"+INPUT_FOLDER+"%",))
results = cur.fetchall()
#for row in results:
#    print(row)

cur.execute("SELECT ZDIRECTORY FROM ZASSET where ZDIRECTORY LIKE ?;" , ("%"+INPUT_FOLDER+"%",))
results = cur.fetchall()
for row in results:
    print(row)

cur.execute("UPDATE ZFILESYSTEMBOOKMARK SET ZPATHRELATIVETOVOLUME = REPLACE(ZPATHRELATIVETOVOLUME,?,?) where ZPATHRELATIVETOVOLUME LIKE ?;" , 
            (INPUT_FOLDER,OUTPUT_FOLDER,"%"+INPUT_FOLDER+"%",))
conn.commit()

cur.execute("UPDATE ZASSET SET ZDIRECTORY = REPLACE(ZDIRECTORY,?,?) where ZDIRECTORY LIKE ?;" , 
            (INPUT_FOLDER,OUTPUT_FOLDER,"%"+INPUT_FOLDER+"%",))
conn.commit()


cur.close()
conn.close()


