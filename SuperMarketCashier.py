def enterProducts():
    buyingData={}
    enterDetails=True
    while enterDetails:
        details=input("Enter A to add the product and Q for quit:")
        if details=="A":
            product=input("Enter the product:")
            quantity=int(input("Enter the quantity:"))
            buyingData.update({product:quantity})
        elif details=="Q":
            enterDetails=False
            break
        else:
            print("Please Enter the correct option")

    return buyingData


def getPrice(product,quantity):
    priceData={
        "wheat":27,
        "rice":30,
        "potato":15,
        "onion":62,
        "mango":40,
        "orange":30,
        "papaya":25
    } 

    subtotal=priceData[product]*quantity
    print("------------------------------------------------------------")
    print(product+":Rs"+str(priceData[product])+"x"+str(quantity)+"="+str(subtotal))
    return subtotal


def getDiscount(billAmount,membership):
    discount=0
    if billAmount>=200:
        if membership=="gold":
           reduct=billAmount*0.80
           discount=20
        elif membership=="silver":
            reduct=billAmount*0.90
            discount=10
        elif membership=="bronze":
            reduct=billAmount*0.95
            discount=5

        print("-----------------------------------------------------------------")
        print(str(discount)+"% off for "+membership+"membership on total amount:Rs"+str(billAmount))
      #  print("-----------------------------------------------------------------")

    else:
        print("billAmount is less than 200")
    
    return reduct


def makeBill(buyingData,membership):
    billAmount=0
    for key,value in buyingData.items():
        billAmount+=getPrice(key,value)
    discountReducted=getDiscount(billAmount,membership)
    print("-----------------------------------------------------------------------")
    print("The Discounted amount is Rs"+str(discountReducted))
    print("-----------------------------------------------------------------------")


buyingData=enterProducts()
membership=input("enter the membership:")
makeBill(buyingData,membership)



