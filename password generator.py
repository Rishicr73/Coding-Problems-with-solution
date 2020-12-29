import random
length = int(input(""))  


lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"
special = "@;.#%*"

all = lower + upper + num + special

password = "".join(random.sample(all,length))
    
print("New password:", password)

    



