#LINK OF THE QUESTION
# https://www.hackerrank.com/challenges/py-the-captains-room/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

#HERE IS CODE

k = int(input())
room = input().split()
sort.room                                                           #Here we are sorting this to get in a correct order
count_room = (set(room[0::2])) ^ (set(room[1::2]))                  #HERE WE HAVE USE SLICING METHOD
print(count_room.pop())                                             #HERE IS POP METHOD IN DICTIONARY WE RETUEN THE REMOVABLE VALUE

