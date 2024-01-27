import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='0000',
                             db='sakila',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()

def add():
   print('you choosed 1, so please input information')
   name_input = input('name: ')
   num_input = input('tel num: ')
   query = "INSERT INTO telbook VALUES (%s, %s)"
   data = (name_input, num_input)
   cursor.execute(query, data)
   print('add complete')

def save():
    print('saved')
    connection.commit()

def printAll():
    cursor.execute("SELECT * FROM `telbook`")
    print("전화번호 데이터를 출력합니다\n")
    print("이름\t 전화")
    print("-------------------------")
  
    row = cursor.fetchone()
    while row:
         print("%s\t %s" % (row['name'], row['num']))
         row = cursor.fetchone()

def delete():
    del_name = input('input name who you wanna delete: ')
    search_query = 'SELECT * FROM telbook WHERE name = %s'
    cursor.execute(search_query, del_name)
    row = cursor.fetchone()
    if row:
         query = 'DELETE FROM telbook WHERE name = %s'
         cursor.execute(query, del_name)
         print("Compeletely Deleted")
    else:
         print('\n해당 데이터가 없습니다')

def search():
    search_data = input('Input Name to Search: ')
    query = 'SELECT * FROM telbook WHERE name = %s'
    cursor.execute(query, search_data)
    row = cursor.fetchone()
    if row:
         print("\n검색 결과\n")
         print("이름\t 전화")
         print("-------------------------")
         while row:
              print("%s\t %s" % (row['name'], row['num']))
              row = cursor.fetchone()
    else:
         print('\n조회된 데이터가 없습니다')
     
print('------ tel book ------')

while True:
   print('\nchoose what do you want to do\n')
   print('1. Add')
   print('2. Delete')
   print('3. Search')
   print('4. Print All')
   print('5. Save')
   print('6. Finish')
   
   choice = int(input('input: '))
   print("\n")
   if choice == 1 :
        add()
   elif choice == 2:
        delete()
   elif choice == 3:
        search()
   elif choice == 4:
        printAll()
   elif choice == 5:
        save()
   else:
        print('shutting down program')
        break

cursor.close()
connection.close()