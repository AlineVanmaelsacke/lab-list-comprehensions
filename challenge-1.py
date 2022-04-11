#!/usr/bin/env python
# coding: utf-8

# ## Challenge 1: Tuples
# 
# #### Do you know you can create tuples with only one element?
# 
# **In the cell below, define a variable `tup` with a single element `"I"`.**
# 
# *Hint: you need to add a comma (`,`) after the single element.*

# In[22]:


# Your code here
tup = ("I",)
tup


# #### Print the type of `tup`. 
# 
# Make sure its type is correct (i.e. *tuple* instead of *str*).

# In[23]:


# Your code here
type(tup)


# #### Now try to append the following elements to `tup`. 
# 
# Are you able to do it? Explain.
# 
# ```
# "r", "o", "n", "h", "a", "c", "k',
# ```

# In[16]:


# Your code here

tup.append("r", "o", "n", "h", "a", "c", "k',)
           
# Your explanation here
# Tuples are immutable and cannot be modified, meaning, they don't accept .append nor .remove
        


# #### How about re-assign a new value to an existing tuple?
# 
# Re-assign the following elements to `tup`. Are you able to do it? Explain.
# 
# ```
# "I", "r", "o", "n", "h", "a", "c", "k"
# ```

# In[25]:


# Your code here

tup = tuple("I",)
new_tup = list(tup)
new_tup = ("I", "r", "o", "n", "h", "a", "c", "k")
tup = tuple(new_tup)

print(tup)
type(tup)


# Your explanation here
# As seen in the previous exercise tuples are immutable and cannot be modified but you can convert the tuple into a list, change the list, 
# and convert the list back into a tuple.


# #### Split `tup` into `tup1` and `tup2` with 4 elements in each. 
# 
# `tup1` should be `("I", "r", "o", "n")` and `tup2` should be `("h", "a", "c", "k")`.
# 
# *Hint: use positive index numbers for `tup1` assignment and use negative index numbers for `tup2` assignment. Positive index numbers count from the beginning whereas negative index numbers count from the end of the sequence.*
# 
# Also print `tup1` and `tup2`.

# In[76]:


# Your code here

tup1 = tup[0:4]
tup2 = tup[4:8]


# #### Add `tup1` and `tup2` into `tup3` using the `+` operator.
# 
# Then print `tup3` and check if `tup3` equals to `tup`.

# In[102]:


# Your code here

tup3 = tup1+tup2
tup3


# #### Count the number of elements in `tup1` and `tup2`. Then add the two counts together and check if the sum is the same as the number of elements in `tup3`

# In[103]:


# Your code here
len(tup1)


# In[104]:


len(tup2)


# In[105]:


len(tup3)


# #### What is the index number of `"h"` in `tup3`?

# In[106]:


# Your code here

index = tup3.index('h')
index


# #### Now, use a FOR loop to check whether each letter in the following list is present in `tup3`:
# 
# ```
# letters = ["a", "b", "c", "d", "e"]
# ```
# 
# For each letter you check, print `True` if it is present in `tup3` otherwise print `False`.
# 
# *Hint: you only need to loop `letters`. You don't need to loop `tup3` because there is a Python operator `in` you can use. See [reference](https://stackoverflow.com/questions/17920147/how-to-check-if-a-tuple-contains-an-element-in-python).*

# In[109]:


# Your code here

letters = ["a", "b", "c", "d", "e"]

for letras in letters:
    if letras in tup3:
        print('True')
    else:
        print('False')


# #### How many times does each letter in `letters` appear in `tup3`?
# 
# Print out the number of occurrence of each letter.

# In[118]:


tup3.count('a')


# In[119]:


tup3.count('b')


# In[120]:


tup3.count('c')


# In[121]:


tup3.count('d')


# In[122]:


tup3.count('e')

