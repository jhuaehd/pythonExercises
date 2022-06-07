#+INdex      0            1        2         3
anime = ["Dragon Ball","Naruto","Kuroko","Haikyuu"]

#anime.clear()
#anime[2] = "kabuto"   assigning a list

#append/add
anime.append("Men")

#count
print(anime.count("Naruto"))

#length
print(len(anime))

#print(anime[1:]) list range

#Insert/Add in a specific indexs
anime.insert(2,"Humba")

#print(anime)

#remove item from list
anime.remove("Humba")


#anime.clear()

food = ["Adobo", "Kinilaw"]

#extend list
#anime.extend(food)

#append list
anime.append(food)

#extracting specific data from a list of a list
print(anime[5][1])