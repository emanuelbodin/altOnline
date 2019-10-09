import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  port=8889,
  database="altOnline"
)

mycursor = mydb.cursor()

def isLeafDepartment(departmentName):
    mycursor.execute("SELECT * FROM departments WHERE parentDepartment=%s", (departmentName,))
    myresult = mycursor.fetchall()
    if (len(myresult) == 0):
        return 1
    return 0

def getDepartmentProducts(departmentName):
    mycursor.execute("SELECT product_title, price_without_tax, discount, tax_to_add FROM products WHERE department=%s", (departmentName,))
    myresult = mycursor.fetchall()
    return myresult

def getChildDepartments(departmentName):
    mycursor.execute("SELECT department_title FROM departments WHERE parentDepartment=%s", (departmentName,))
    myresult = mycursor.fetchall()
    return myresult

def getProductDiscount(productTitle):
    mycursor.execute("SELECT discount FROM products WHERE product_title=%s", (productTitle,))
    myresult = mycursor.fetchall()
    for x in myresult:
        return x

def setDiscount(productTitle, discount):
    mycursor.execute("UPDATE products SET discount = %s WHERE product_title=%s", (discount, productTitle,))
    mydb.commit()

print(isLeafDepartment('IPads'))

while (1):
    toDo = input("Do you want to list all products from a departemt or set discount for a specific product? (type y or n)")
    if (toDo == 'y'):
        department = input("Enter a department:")
        if (isLeafDepartment(department)):
            products = getDepartmentProducts(department)
            print("The " + department + " have the following products:")
            for product in products:
                price = int(round((float(product[1]) * (1 - 0.01 * float(product[2])) * (1 + 0.01 * float(product[3])))))
                print(product[0] + ", price: " + "$" + str(price))
        else:
            childDepartments = getChildDepartments(department)
            print('Departments: ')
            for child in childDepartments:
                print(child[0])
    elif (toDo == 'n'):
        productTitle = input("Enter a product title to get it's discount: ")
        discount = getProductDiscount(productTitle)[0]
        print("The discount for " + productTitle + " is " + str(discount)+ "%")
        ans = input("Do you want to update the discount? (y for yes or n for no)")

        if (ans == 'y'):
            newDiscount = input("Enter new discount:")
            setDiscount(productTitle, newDiscount)
            newDiscount = getProductDiscount(productTitle)[0]
            print("New discount for " + productTitle + " is " + str(newDiscount) + "%")
        else:
            print('Bye!')
    else:
        print("Error, you should press y or n")
