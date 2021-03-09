from Invoice import Invoice

products = {}
total_amount = 0
repeat = ''
while True:
    product = input('what is your product : ')
    unit_price = Invoice().inputNumber("Please enter unit price : ")
    qnt = Invoice().inputNumber("please enter quantity of product : ")
    discount = Invoice().inputNumber("Discount (%) : ")
    repeat = Invoice().inputAnswer("Another product? (y,n) : ")
    result = Invoice().addProduct(qnt, unit_price, discount)
    products[product] = result
    if repeat == 'n':
        break

total_amount = Invoice().totalImpurePrice(products)
average = Invoice().averagePrice(products)
high = Invoice().highestItemPrice(products)
print("your total pure price is: ", total_amount)
print("The average price per item is:  " + str(average))
print(high)
