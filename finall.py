
#from pyfiglet import Figlet
def add():
     num_goods=int(input("enter number of goods for adding"))  
     for i in range(num_goods):
      myadd={}
      myadd["id"]=int(input("enter id:"))
      myadd["name"]=str(input("enter name of goods:"))
      myadd["price"]=int(input("enter price:"))
      myadd["count"]=int(input("enter count:"))
      PRODUCT.append(myadd)
     print(PRODUCT)

def menu_edit():
   print(" 1 for edit name")
   print(" 2 for edit price")
   print(" 3 for edit count")       

def edit():
   id_edit=input("enter the id good:")
   for i in range(len(PRODUCT)):
     if id_edit==PRODUCT[i]["id"]:
        menu_edit()
        select_menuedit=int(input("enter your select:")) 
        if select_menuedit==1:
           new_name=str(input("enter new name:"))
           PRODUCT[i]["name"]=new_name
           print(PRODUCT)

        elif select_menuedit==2:
          new_price=int(input("enter new price:"))
          PRODUCT[i]["price"]=new_price
          print(PRODUCT)

        elif select_menuedit==3:
          new_count=int(input("enter new count:"))
          PRODUCT[i]["count"]=new_count
          print(PRODUCT)

def delete(): 
    delet_goods=int(input("enter id of goods for delete:"))  
    for i in range(len(PRODUCT)):
     if  delet_goods==PRODUCT[i]["id"]: 
        PRODUCT.pop[i]
        print(PRODUCT)  
        break  
    
def search():
    search_name=input("enter the goods name for search:")
    for i in range(len(PRODUCT)):
     if search_name==PRODUCT[i]["name"]:
      print("the good is found:",PRODUCT[i])   

        
def show_menu():
    print("1- Add product")
    print("2- Edit product")
    print("3- Delete product")
    print("4- Search")
    print("5- Show list")
    print("6- Buy")
    print("7- exit")

myfile=open("databasef.txt","r")
data=myfile.read()

PRODUCT = []
product_list = data.split("\n")

for i in range (len(product_list)):
    product_info  =product_list[i].split(",")
    mydict = {}
    mydict["id"]=product_info[0]
    mydict["name"]=product_info[1]
    mydict["count"]=product_info[2]
    mydict["price"]=product_info[3]
    PRODUCT.append(mydict)
   

#f = Figlet(font= "standard")
#print(f.renderText("Store"))
while True:
 show_menu()
 choice = int(input("please choice a number:"))

 if choice == 1:
    add()
 elif choice == 2:
    edit()
 elif choice == 3:
    delete()
 elif choice == 4:
    search()
 elif choice == 5:
    pass
 elif choice == 6:
    pass
 elif choice ==7:
    pass