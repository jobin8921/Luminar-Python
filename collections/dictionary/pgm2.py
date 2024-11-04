
# mobiles = {"Apple":{"model":"iphone15","price":120000,"color":"Black"},
#            "Samsung":{"model":"s23","price":180000,"color":"White"},
#            "Sony":{"model":"xperia","price":130000,"color":"red"},
#            "Huawei":{"model":"pura 70 ultra","price":170000,"color":"Black"}}

# print(mobiles["Apple"]["model"])       

# filter the mobilw which has black in colour

# mobiles["Apple"]["model"] = "iphone 16 pro max"

# for i in mobiles.keys():

#     if mobiles[i]["color"]=="Black":

#         print(f"{i} : {mobiles[i]}")


# filter the item which is less than 150000

# for i in mobiles.keys():

#     if mobiles[i]["price"] < 150000:

#         print(f"{i} : {mobiles[i]}")

# filter the items with price > 150000 and colour is white

# for i in mobiles.keys():

#     if mobiles[i]["price"] > 150000 and mobiles[i]["color"] == "white":

#      print(f"{i} : {mobiles[i]}")



mobiles = {"Apple":{"model":"iphone15","price":120000,"colors":["Black","Red","Golden"]},
           "Samsung":{"model":"s23","price":180000,"colors":["Yellow","Red","White"]},
           "Sony":{"model":"xperia","price":130000,"colors":["Black","Orange","Golden"]},
           "Huawei":{"model":"pura 70 ultra","price":170000,"colors":["Black","Brown","White"]}}

# mobiles["Sony"]["colors"][1] = "white"\

# print(mobiles["Sony"]["colors"][1])  # Output: white

# filter the element with black color available

# for i in mobiles.keys():

#     if "Black" in mobiles[i]["colors"]:

#         print(f"{i} : {mobiles[i]}")


# filter the mobile with price > 150000, with black or red in color
for i in mobiles.keys():

    if mobiles[i]["price"] > 150000 and ("Black" or "red" in mobiles[i]["colors"]):

       print(f"{i} : {mobiles[i]}")
        

