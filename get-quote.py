def main()
  import random
  last=13
  rnd = random.randint(0,last)
   print("Random quote bot is working")

   f = open("quotes.txt")
   quotes = f.readlines()
   f.close()

   print(quotes[rnd])

if __name__== "__main__":
  main()
