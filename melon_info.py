"""Print out all the melons in our inventory."""


from melons import melon_inventory

      
# Iterates through inventory. Prints melon type.     
for melon in melon_inventory:
    print(melon)

    # Unpacks and prints tuple for each melon in melon_inventory. 
    for data, attrib in melon_inventory[melon].items():
        print(f"{data} : {attrib}")

    print()

