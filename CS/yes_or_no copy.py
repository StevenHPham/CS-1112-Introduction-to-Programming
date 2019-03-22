looking = True

while looking:
   reply = input("yes or no: ")
   reply = reply.lower()
   if reply in (['yes','no']):
      looking = False

      print(reply)
