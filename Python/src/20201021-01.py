##--------------#-----------------------------------------------------------#
#|              | CLASS SAMPLE FOR "COMPUTER SCIENCES" (07JCJ**)            #
#|   ######     | (!) 2020, Giovanni Squillero <squillero@polito.it>        #
#|  #######     | https://github.com/squillero/computer-sciences            #
#|  ####   \    |                                                           #
#|   ###G  c\   | => Copying and distributing this file for classroom use,  #
#|   ##     _\  | either with or without modification, is permitted without #
#|   |    _/    | royalties provided that this 11-line comment is preserved #
#|   |   _/     |                                                           #
#|              | => THIS FILE IS OFFERED AS-IS, WITHOUT ANY WARRANTY       #
##--------------#-----------------------------------------------------------#

foo = 4
bar = 2

print("The answer is \"{foo*10 + bar:10d}\"")
print(f"The answer is \"{foo*10 + bar:10d}\"")
print("The answer is", foo*10 + bar)

s1 = f"{foo*10 + bar}"
s2 = f"{foo*10 + bar:e}"
s3 = f"{foo*10 + bar:20.4f}"

print(s1)
print(s2)
print(s3)

print(f"{round(2/3):d}")
