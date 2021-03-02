## Shop Appender
## By TechLife#6902 on Discord
## Made to work with Unprotesting's Auto-Tune

import itertools
import csv

item = ""
fileList = []

print("\nEnter STOP to stop adding items and save the file.")
print("CSV files should be in the format \n")
path = input("Enter the path of your shops.yml file e.g. D:/Server/plugins/Auto- Tune/shops.yml\nNote: I would recommend using a copy of the shops.yml file to avoid problems: ")
print("\n")

with open(path,"r",encoding='utf-8') as file:
    fileList = file.readlines()

mode = input("Choose the mode you want to use.\nMANUAL for manual text input or CSV for CSV import: ").upper()
print("\n")

if mode == "MANUAL":
    line = int(input("Enter the line number to start adding from: (should be blank and below other items) "))-1
    while item != "STOP":
        item = input("Item name: ").upper()
        if item == "STOP":
            break
        price = float(input(f"{item} price: "))
        maxBuy = int(input(f"Maximum {item}S available to buy: "))
        maxSell = int(input(f"Maximum {item}S available to sell: "))
        section = input("Section (must be pre-existing): ")
        fileList.insert(line,f"  {item}:"+"\n")
        fileList.insert(line+1,f"    price: {price}"+"\n")
        fileList.insert(line+2,f"    max-buy: {maxBuy}"+"\n")
        fileList.insert(line+3,f"    max-sell: {maxSell}"+"\n")
        fileList.insert(line+4,f"    section: '{section}'"+"\n")
        line +=5
        print("Item added.\n")
    
    with open(path,"w",encoding='utf-8') as file:
        file.writelines(fileList)
    print("\nFile updated successfully.")
    input("\nPress ENTER to quit.")

elif mode == "CSV":
    csvPath = input("Enter the path to your CSV file.\nEnsure the CSV file is in the format itemid,price,max-buy,max-sell,section otherwise the program will not work: ")
    print("\n")
    line = int(input("Enter the line number of the shops.yml file to add the items too.\nThis should be blank and below 'shops:' (if no other items are present):"))
    with open(csvPath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                tempList = []



