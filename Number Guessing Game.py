#!/usr/bin/env python
# coding: utf-8

# In[29]:


class Number_Guessing_Game:
    def __init__(self):
        pass
    
    def guess(self):
        guess = int(input("Guess the secret number?"))
        if guess==30:
            print("You have guessed the secret number.")
        else:
            print("Try again.")


# In[30]:


Number_Guessing_Game.obj = Number_Guessing_Game()


# In[33]:


Number_Guessing_Game.obj.guess()


# In[ ]:




