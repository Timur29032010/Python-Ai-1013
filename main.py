class Dog:

   def __init__(self,name):

       self.name = name

       self.hungry = True

       self.tired = True

       self.happy = False


   def food(self):

       if self.hungry:

           print(f"{self.name} Hungry and crazy.")

           self.hungry = False

       else:

           print(f"{self.name} is not hungry.")


   def sleep(self):

       if self.tired:

           print(f"{self.name} has gone to sleep.")

           self.tired = False

       else:

           print(f"{self.name} is not tired.")


   def play(self):

       if self.happy:

           print(f"{self.name} is already playing.")

       else:

           print(f"{self.name} is playing now.")

           self.happy = True