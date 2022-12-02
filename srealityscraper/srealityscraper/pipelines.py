from itemadapter import ItemAdapter
import psycopg2

class SrealityPipeline:

    def __init__(self): # db creation and connection
        hostname = '127.0.0.1'
        port = '8042'
        username = 'pi'
        password = 'lolipoplove'
        database = 'sreality'
        # conn to the db
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port)
        self.cur = self.connection.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS flat(
            id serial PRIMARY KEY,
            title text,
            image_urls text
        )
        """)
        print('TABLE flat created!')
        self.cur.execute("""
        DELETE FROM flat *
        """) 

    def process_item(self, item, spider): #from http response we retrive and send the data to the database
        #insert to the db
        self.cur.execute(""" insert into flat (title, image_urls) values (%s,%s)""", (
            item["title"],
            str(item["image_urls"])
        ))
        #insertion
        self.connection.commit()
        print('proccessed')
        return item

    def close_spider(self, spider): # Generise html od vrijednosti povucenih iz baze
        # html priprema za bazu
        self.cur.execute("""
        SELECT * FROM flat
        """)
        print("ROws and flats")
        flat_records = self.cur.fetchall()

        print("row and values from the column")
        for row in flat_records: 
            print("Title = ", row[1], )
            print("Image urls = ", row[2], "\n")
            
        strTable = "<html><meta charset=\"UTF-8\"><table><tr><th>Flats</th><th> </th></tr>"
        for row in flat_records:
            strRW = "<tr><td>"+row[1]+ "</td><td><img src=\""+row[2]+"\"></td></tr>"
            strTable = strTable+strRW
     
        strTable = strTable+"</table></html>"
     
        hs = open("../../server/srealityFlats.html", 'w')
        hs.write(strTable)
        hs.close()
        
        self.cur.close()
        self.connection.close()