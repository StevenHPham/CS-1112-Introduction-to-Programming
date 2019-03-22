
''' Purpose: demonstrate while loop and dict mappings
    Name: Steven Pham

    Email id: shp4df
'''

# get url reading abilities
import url

# where is the commodity cost mappings
COMMODITIES_CSV = 'http://www.cs.virginia.edu/~cs1112/datasets/csv/commodities.csv'

# get web-based commodities dataset 
dataset = url.get_dataset( COMMODITIES_CSV )

# convert dataset into commodity cost mappings dictionary
commodity_mappings = {}

truther = True

while truther:
    reply = input("Enter commodity: ")
    reply = reply.lower()
    reply = reply.strip()
    price = commodity_mappings.get(reply)
    for commodity in dataset:
        item, price = commodity
        commodity_mappings[item] = price
    if reply in commodity_mappings:
        print(price)
    elif reply == "":
        truther = False
    elif reply not in commodity_mappings:
        print("pricing unknown")



# while user is supplying queries, process them. user indicates no more
# queries by not entering an empty response

# all done

