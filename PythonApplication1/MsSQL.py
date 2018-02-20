import pymssql


def to_sql(data):
    #conn=MySQLdb.connect("localhost","root","wangwust","test",charset="utf8" )
    conn = pymssql.connect(host='localhost',user='sa',password='123',database='test')
    cursor = conn.cursor()
    cursor.execute('''create table test.tiger_book2(book_id bigint,
                                                    title varchar(50),
                                                    author varchar(50),
                                                    types varchar(30),
                                                    status varchar(20),
                                                    words decimal(8,2),
                                                    cliks decimal(10,2),
                                                    recoms decimal(8,2),
                                                    votes varchar(20),
                                                    score varchar(20),
                                                    info varchar(3000));''')
    cursor.executemany('insert into test.tiger_book2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);',data)
    #cursor.execute('select * from test.tiger_book2 limit 5;')
 
    conn.commit()
    cursor.close()
    conn.close()

data = [[],[],[],[]]
to_sql()