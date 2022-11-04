#!/usr/bin/env python
# coding: utf-8

# Problem1: Basketball Score Calculator

# In[63]:


import sys, argparse
try:
    parser=argparse.ArgumentParser()
    parser.add_argument('two',type=int)
    parser.add_argument('three',type=int)
    parser.add_argument('one',type=int)
    args=parser.parse_args()
    total=(args.two)*2+(args.three)*3+(args.one)
    print(total)
except Exception as e:
    print(e)

# Problem2: Body Mass Index Calculator

# In[ ]:


import sys
def healthStatus(height,mass):
    BMI=mass/(height*2)
    if BMI<18.5:
        sys.stdout.write("'underweight'")
    if BMI>=18.5:
        if BMI<24.9:
            sys.stdout.write("'healthy'")
    if BMI>=24.9:
        if BMI<30:
            sys.stdout.write("'overweight'")
    if BMI>=30:
        sys.stdout.write("'obese'")
    return


# %%
