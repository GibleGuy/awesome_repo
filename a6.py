import math
import random as rn
import numpy as np
# import matplotlib.pyplot as plt
import os 
import csv


print(os.getcwd())

# PROBLEM ONE

data = []
#INPUT path and filename
#OUTPUT list of parent, child pairs
#CONSTRAINT use csv reader
def get_data(path, filename):
    with open(path+filename) as magic:
        reading = csv.reader(magic)
        return list(reading)



#input parent name
#output children
#constraint using comprehension
def get_child(name):
    return [i[1] for i in data if name == i[0]]


#input parent name
#output true if has children
#constraint using comprehension
def has_children(name):
    return bool(get_child(name))


#input child name
#output parent of child
#constraint using comprehension
def get_parent(name):
    return [i[0] for i in data if name == i[1]]


#input child name1, child name2
#output true if children have same parent
#constraint using comprehension
def siblings(name1,name2):
    return get_parent(name1) == get_parent(name2) 
 
#input grandparent name1, grandchild name2
#output true if name1 is grandparent to name2
#constraint using comprehension 
def grandparent(name1, name2):
    return name1 == get_parent(get_parent(name2)[0])[0]

#input nothing
#output all names
#constraint list comprehension only
def get_all():
    return [k for k in [i for i,j in data] + [j for i,j in data]]

#input name1, name2
#output true if name1 and name 2 are cousins, i.e., have the same grandparents
def cousins(name1,name2):
    return get_parent(get_parent(name1)[0]) == get_parent(get_parent(name2)[0])


# Problem 2
# input n: total space (size), v: tiles and 
# output all possible patterns where the tiles add exactly to the the space (n)
def tiles(n, v, lst):
    # lst = [[i] for i in v]
    for _ in range(n):
        for item in lst:
            if not sum(item) == n:
                for number in v:
                    temp = item + [number]
                    if sum(temp) <= n and (temp not in lst):
                        lst = lst + [temp]
            if not sum(item) == n:
                lst.remove(item) 
    lst.sort(reverse=True)
    return lst
            
    # print(f"{lst} THIS IS THE LIST")
    # templst = []
    # for x in lst:
    #     if sum(x) == n:
    #         templst = templst + [x]
    # templst.sort(reverse=True)
    # finallst = templst
    # # for j in templst:
    #     if j not in finallst:
    #         finallst = finallst + [j]
                

    '''I made a version of this function
    that randomly goes through every possible combination
    and outputs the correct ones'''

    # final = []
    # escape = 0
    # finish = 0
    # temp = []
    # while finish < 10000:
    #     escape = 0
    #     temp = []
    #     while escape == 0:
    #         temp = temp + [rn.choice(v)]
    #         if sum(temp) > n:
    #             escape = 1
    #         elif sum(temp) == n and temp not in final:
    #             final = final + [temp]
    #             escape = 1
    #     finish += 1
    #     print(f"this function has ran {finish} times")
    # final.sort(reverse=True)
    # return final



#problem 3
# input: a list of numbers
# output: a pair containing the sum and boolean vector (see PDF for sample output)
def max_adjacent(lst):
     # coollst = [] + lst
    # for x in coollst:
    #     if len(x) > 2:
    #         coollst = coollst + [x[1:]]
    #     for y in len(x):
    #         coollst = coollst + [x[0] + x[1]]
    pass
    #     #idk man I tried




########################
# PROBLEM 4
########################


# INPUT path and filename (payrollwins.txt)
# OUTPUT payroll and number of wins as a list
# Ouptut example: [[209,89], [139,74]]
# CONSTRAINT use csv reader
def get_data_1(path, filename):
    with open(path+filename) as magic:
        reading = csv.reader(magic)
        return [[int(i[0]),int(i[1])] for i in reading]
        


#INPUT data points (x0,y0),...,(xn,yn)
#OUTPUT best regression slope m_hat, intercept b_hat, and R_sq
def std_linear_regression(data):

    xyp=xs=ys=xsq=sst=sse=ysq=0
    for i in data:
        x,y = i
        xyp += x*y
        xs += x
        ys += y
        xsq += x**2
        ysq += y**2
    sxy = xyp - ((xs*ys)/len(data))
    sxx = xsq - ((xs**2)/len(data))
    m_hat = round(sxy / sxx, 3)
    b_hat = round((ys-(m_hat*xs))/len(data),3)
    sst = ysq - (ys**2/len(data))
    sse = ysq - (b_hat*ys) - (m_hat*xyp)
    R_sq = round((sst-sse)/sst,3)
    # for i in data:
    #     x,y = i
    #     x,y = int(x),int(y)
    #     sst += (y**2)-((ys**2)/len(data))
    #     sse += (y**2) - b_hat*ys - m_hat*xyp
    #     
        
    return m_hat, b_hat, R_sq



#### Problem 5

# INPUT path and filename (fish_data.txt)
# OUTPUT two separate lists, first one containing the age and second containing 
# the length as given in the fish_data.txt file 
# Ouptut example: [1,2,3, ...], [4.8, 8.8, 8.0, ...]
# CONSTRAINT use csv reader
# make sure to get rid of the first line that just contains the column names (we don't want that)
def get_fish_data(path, name):
    with open(path+name) as magic:
        reading = csv.reader(magic)
        cow = [x for x in reading]
        cow = cow[1:]
        awesome = [[i[0],i[1]] for i in cow]
        ages = [int(x[0]) for x in awesome]
        lengths = [float(x[1]) for x in awesome]
        return ages, lengths

#INPUT lists X values, Y values of data and degree of the polynomial
#RETURN a polynomial of degree three
def make_function(X,Y,degree):
    return np.poly1d(np.polyfit(X,Y,degree))
    # return np.polyfit(X,Y,degree)
    


#### Problem 6
#input string and positive integer n
#output a list of the longest string that have no more than n distinct symbols

def max_n(str, n):
    long = []
    max = 0
    start = 0
    totalchar = {}
    holdlst = []
    for i in str:
        if i not in holdlst:
            holdlst = holdlst + [i]

    if len(holdlst) < n:
        return [""]

    for end in range(len(str)):
        char = str[end]

        if char not in totalchar:
            totalchar[char] = 0

        totalchar[char] += 1

        while len(totalchar) > n:
            start_char = str[start]
            totalchar[start_char] -= 1
            if totalchar[start_char] == 0:
                del totalchar[start_char]
            start += 1

        current_length = end - start + 1

        if current_length > max:
            max = current_length
            long = [str[start:end+1]]
        elif current_length == max:
            long.append(str[start:end+1])
    long = list(dict.fromkeys(long))    
    return long



#problem 7

#input a tuple of model parameters, second parameter is the number of trials
#output the percent success rounded to two decimal places
def simulation(model_parameters, num_trials):
    # def win(b,p,m):
    #     return (1-math.pow((1-p)/p,b))/(1-math.pow((1-p)/p,m))
    # print(win(*model_parameters))


    b,p,m = model_parameters
    return round(sum(np.random.binomial(1,(1-(((1-p)/p)**b)) / (1-(((1-p)/p)**m)),(num_trials*10)) == 1)/(num_trials*10),2)

 
    # for _ in range(num_trials):
    #     run_sim(model_parameters)






if __name__ == '__main__':
    
    # uncomment to test
    # Before sbmitting to the Autograder: 
    # Make sure to comment the code for plotting graph in P4 and also the import of matplotlib on the top of this file
    # You can use that code to make the graph on your system and test but comment it before the submission

    # problem 1
    # data = get_data("Assignment6\\", "family.txt")
    # print(data)
    # # print(has_children('0')) #true
    # # print(has_children('7')) #false
    # # print(get_child('6')) #7, a, g
    # print(get_parent('g')) #6
    # print(siblings('7','A')) #true
    # print(siblings('2','7')) #false
    # print(grandparent('0','3')) #true
    # print(grandparent('0','7')) #false
    # print(get_all())
    # print(cousins('3','6')) #true
    # print(cousins('3','5')) #false


    # problem 2
    # n = 6
    # v = [1,2,3]
    # print(tiles(n,v,[[i] for i in v]))
    # for i in tiles(n,v,[[i] for i in v]):
    #     print(sum(i), end="")
    # n = 4
    # v = [1,2]
    # print(tiles(n,v,[[i] for i in v]))
    # for i in tiles(n,v,[[i] for i in v]):
    #     print(sum(i), end="")    
    print(tiles(6, [ 1, 4 ], [ [ 1 ], [ 4 ] ]))

    #problem 3
    # data = [[5,1,4,1,5],[5,6,2,4],[4,5,1,1],[1,5,10,4,1],[1,1,1,1,1]]
    # for d in data:
    #     print(max_adjacent(d))

    #problem 4

    # data6 = get_data_1("Assignment6\\", "payrollwins.txt")
    # print(data6)
    # m_hat, b_hat, R_sq  = std_linear_regression(data6)
    # print(m_hat,b_hat,R_sq)
    
    # Comment the code for plotting (and the import of matplotlib up top) before you submit to the Autograder.
    # You can test as much as you want on your system but before the submission - please comment the code for
    # plotting.
    # plt.plot([x for x,_ in data6],[y for _,y in data6],'ro')
    # plt.plot([x for x,_ in data6],[m_hat*x + b_hat for x,_ in data6],'b')
    # plt.xlabel("$M Payroll")
    # plt.ylabel("Season Wins")
    # plt.title(f"Least Squares: m = {m_hat}, b = {b_hat}, R^2 = {R_sq} ")
    # plt.ylabel("Y")
    # plt.show()

    # #problem 5
    # name = "fish_data.txt"
    # X,Y = get_fish_data("Assignment6\\", name)
    # data5 = [[i,j] for i,j in zip(X,Y)]
    # print(data5)
      
    # plt.plot(X,Y,'ro')
    # xp = np.linspace(1,14,10)
    # degree = 3
    # p3 = make_function(X,Y,degree)
    # plt.plot(xp,p3(xp),'b')
    # plt.xlabel("Age (years)")
    # plt.ylabel("Length (inches)")
    # plt.title("Rock Bass Otolith")
    # plt.show()

    #problem 6
    # data = ["aaaba", "abcba", "abbcde","aaabbbaaaaaac","abcdeffg"]
    # for d in data:
    #     for i in range(1,7):
    #         print(f"{d} with {i} max is\n {max_n(d,i)}")
    
    
    #problem 7
    # model_parameters = (2,.6,4) #starting amount, probablity of win, goal
    # print(simulation(model_parameters,100000))

    print()
