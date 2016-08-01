import sqlite3,random
def activation_generator():
    return str(random.randrange(0,100000))

if __name__=='__main__':
    conn = sqlite3.connect('activation_code.db')
    cursor = conn.cursor()
    try:
        cursor.execute('create table activation_key (id vchar(10) primary key,code vchar(20))')
    finally:
        exit()

    for i in range(200):
        insert = "insert into activation_key (id,code) values (\'{0}\',\'{1}\')".format(str(i),activation_generator())
        cursor.execute(insert)
    cursor.close()
    conn.commit()
    conn.close()
