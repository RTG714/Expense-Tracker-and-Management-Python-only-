print("================ EXPENSE TRACKER ================")

salary=float(input("Enter your salary:"))
savings=float(input("Enter your ideal savings (Expense should not go above this limit):"))
zomato=float(input("Enter your monthly zomato expense:"))
restaurant=float(input("Enter your monthly restaurant expense:"))
veggies=float(input("Enter your monthly expense on fruits and vegetables:"))
uber=float(input("Enter your monthly uber expense:"))
fuel=float(input("Enter your monthly fuel expense:"))
metro=float(input("Enter your monthly metro expense:"))
online=float(input("Enter your monthly online shopping expense:"))
groceries=float(input("Enter your monthly grocery expense:"))
clothing=float(input("Enter your monthly clothing expense:"))
electricity=float(input("Enter your monthly electricity expense:"))
wifi=float(input("Enter your monthly wifi expense:"))
network=float(input("Enter your monthly network expense:"))
water=float(input("Enter your monthly water expense:"))
ott=float(input("Enter your monthly OTT expense:"))
tv=float(input("Enter your monthly tv expense:"))
spotify=float(input("Enter your monthly spotify expense:"))

print("\n\n")

expense=0
category={}

def updateglobal():
    global expense
    global category

    expense=zomato+restaurant+veggies+uber+fuel+metro+groceries+online+clothing+electricity+wifi+network+water+ott+tv+spotify

    category={"FOOD":{"Zomato":zomato,"Restaurant":restaurant,"Veggies":veggies},
          "TRANSPORT":{"Uber":uber,"Fuel":fuel,"Metro":metro},
          "SHOPPING":{"Online":online,"Groceries":groceries,"Clothing":clothing},
          "BILLS":{"Electricity":electricity,"WiFi":wifi,"Network":network,"Water":water},
          "ENTERTAINMENT":{"OTT":ott,"TV":tv,"Spotify":spotify}}

updateglobal()

def record():
    for x,y in category.items():
        print("=========",x,"=========")
        for j in y:
            print(j+" -",y[j])

record()

print("\n\n")

def alterfood():
    ch=int(input("Which food expense would you like to alter?\n1. Zomato\n2. Restaurant\n3. Fruits & Vegetables\nEnter your choice:\n"))
    if ch==1:
        global zomato
        zomato=float(input("Enter your monthly zomato expense:"))
    elif ch==2:
        global restaurant
        restaurant=float(input("Enter your monthly restaurant expense:"))
    elif ch==3:
        global veggies
        veggies=float(input("Enter your monthly expense on fruits and vegetables:"))
    else:
        print("Invalid choice")
    updateglobal()
    print("\n\n")
 
def altertransport():
    ch=int(input("Which transportation expense would you like to alter?\n1. Uber\n2. Fuel\n3. Metro\nEnter your choice:\n"))
    if ch==1:
        global uber
        uber=float(input("Enter your monthly uber expense:"))
    elif ch==2:
        global fuel
        fuel=float(input("Enter your monthly fuel expense:"))
    elif ch==3:
        global metro
        metro=float(input("Enter your monthly metro expense:"))
    else:
        print("Invalid choice")
    updateglobal()
    print("\n\n")

def altershop():
    ch=int(input("Which shopping expense would you like to alter?\n1. Online\n2. Groceries\n3. Clothing\nEnter your choice:\n"))
    if ch==1:
        global online
        online=float(input("Enter your monthly online expense:"))
    elif ch==2:
        global groceries
        groceries=float(input("Enter your monthly groceries expense:"))
    elif ch==3:
        global clothing
        clothing=float(input("Enter your monthly clothing expense:"))
    else:
        print("Invalid choice")
    updateglobal()
    print("\n\n")

def alterbill():
    ch=int(input("Which bill expense would you like to alter?\n1. Electricity\n2. Wi-Fi\3. Network\n4. Water\nEnter your choice:\n"))
    if ch==1:
        global electricity
        electricity=float(input("Enter your monthly electricity expense:"))
    elif ch==2:
        global wifi
        wifi=float(input("Enter your monthly Wi-Fi expense:"))
    elif ch==3:
        global network
        network=float(input("Enter your monthly network expense:"))
    elif ch==4:
        global water
        water=float(input("Enter your monthly water expense:"))
    else:
        print("Invalid choice")
    updateglobal()
    print("\n\n")

def alterentertainment():
    ch=int(input("Which entertainment expenses would you like to alter?\n1. OTT\n2. TV\n3. Spotify\nEnter your choice:\n"))
    if ch==1:
        global ott
        ott=float(input("Enter your monthly ott expense:"))
    elif ch==2:
        global tv
        tv=float(input("Enter your monthly tv expense:"))
    elif ch==3:
        global spotify
        spotify=float(input("Enter your monthly spotify expense:"))
    else:
        print("Invalid choice")
    updateglobal()
    print("\n\n")

def check():
    if (salary-expense)>savings:
        print("Good management!")
    else:
        print("Dangerous management!")
    print("\n\n")

def function():
    flag=True
    while flag==True:
        ch=int(input("What would you like to do with your expenses?\n1. Alter Expenses\n2. Display Expenses\n3. Check stability\n4. Exit\nEnter your choice:\n"))
        if ch==1:
            cho=int(input("What would you like to alter?\n1. FOOD\n2. TRANSPORT\n3. SHOPPING\n4. BILLS\n5. ENTERTAINMENT\nEnter your choice:\n"))
            if cho==1:
                alterfood()
            elif cho==2:
                altertransport()
            elif cho==3:
                altershop()
            elif cho==4:
                alterbill()
            elif cho==5:
                alterentertainment()
            else:
                print("Invalid choice")
        elif ch==2:
            record()
        elif ch==3:
            check()
        elif ch==4:
            print("Thank you for using my interface!")
            flag=False

function()

print("\n\n")
