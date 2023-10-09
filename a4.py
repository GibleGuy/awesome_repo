import math
import matplotlib.pyplot as plt
import cmath


###########################################################################
# Functions for Problem 1
###########################################################################
#INPUT dlst = [day, month, year]
#RETURN string corresponding to the day of the week (i.e. "Mon", "Sun", etc)
week = {1:"Mon", 2:"Tue", 3:"Wed", 4:"Thu", 5:"Fri", 6:"Sat", 7:"Sun"}
def a(dlst):
    d,m,y = dlst
    return y-(14-m)/12

def b(dlst):
    x = a(dlst)+a(dlst)/4-a(dlst)/100+a(dlst)/400
    return math.floor(x)

def c(dlst):
    d,m,y = dlst
    return m + 12*((14/m)/12)-2

def day(dlst):
    d,m,y = dlst
    return week[math.floor((d+b(dlst)+ (31*c(dlst)/12))%7)-1]


###########################################################################
# Functions for Problem 2
###########################################################################
#INPUT t = (a,b,c)
#RETURN return complex or real roots
def q(t):
    a,b,c = t

    sim_root = b*b-(4*a*c)    

    if sim_root >= 0:
        sim_root = math.sqrt(b*b-(4*a*c))
        pos_answ = round((-b+sim_root)/(a*2),2)
        neg_answ = round((-b-sim_root)/(a*2),2)
        if pos_answ > neg_answ:
            return (neg_answ, pos_answ)
        else:
            return (pos_answ, neg_answ)
    else:
        pos_root = (-b + cmath.sqrt(b*b-4*a*c))/(2*a)
        neg_root = (-b - cmath.sqrt(b*b-4*a*c))/(2*a)
        pos_root = round(pos_root.real, 2) + round(pos_root.imag, 2) * 1j
        neg_root = round(neg_root.real, 2) + round(neg_root.imag, 2) * 1j
        return (pos_root, neg_root)






###########################################################################
# Functions for Problem 3
###########################################################################
#INPUT a nested list of people encoded as 0's and 1's. v0 and v1 are the respective lists respresenting the people pairs.
# You'll be comparing the smallest degree of difference between each sublist representing each person.
# RETURN person pair with the smallest degree (smallest degree of difference between the person pair lists)
def inner_prod(v0,v1):
    sum = 0
    tmp = 0
    while tmp < len(v0):
        sum += v0[tmp]*v1[tmp]
        tmp += 1
    return sum

def mag(v):
    return math.sqrt(inner_prod(v,v))

def angle(v0,v1):
    return round(math.acos(round(inner_prod(v0,v1)/(mag(v0)*mag(v1)),10))*180/math.pi,2)

def match(people):
    tmp = 0
    second = 1
    output = []
    while tmp < len(people):
        while second < len(people):
            output += [[people[tmp], people[second], angle(people[tmp],people[second])]]
            second += 1
        tmp += 1 
        second = tmp+1
    return output

def best_match(scores):
    tmp = 10000
    storage = ['cows']
    for i in scores:
        hold = i[2]
        if hold < tmp:
            tmp = hold
            storage = i
    return storage




###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT tuple of quadratic (ax^2 + bx + c)
#RETURN tuple (m,n) cofficients for real solutions a(x+m)^2 + n = 0
#CONSTRAINT round to 2 places
def c_s(coefficients):
    a, b, c = coefficients
    m = b/(a*2)
    n = c-((b*b)/(4*a))
    return (round(m,2), round(n,2))


#INPUT coefficients for quadratic ax^2 + bx + c 
#RETURN return real roots uses c_s
def q_(coefficients):
    m,n = c_s(coefficients)
    posx = -m + math.sqrt(-n)
    negx = -m - math.sqrt(-n)
    return (round(posx, 2), round(negx, 2))


###########################################################################
# Functions for Problem 5
###########################################################################
# INPUT List of numbers
# RETURN Various means
def mean(lst):
    return round(sum(lst)/len(lst),2)

def var(lst):
    mu = mean(lst)
    sum = 0
    starter = 1/len(lst)
    for i in lst:
        sum += pow((i - mu),2)
    return round(starter*sum,2)


def std(lst):
    return round(math.sqrt(var(lst)),2)

def mean_centered(lst):
    mu = mean(lst)
    returnee = []
    for i in lst:
        returnee += [i-mu]
    return returnee



###########################################################################
# Functions for Problem 6
###########################################################################
# INPUT supply and demand coefficients
# RETURN solution of quadratic equations
def equi(s,d):
    equation = (s[0]-d[0],s[1]-d[1],s[2]-d[2])
    answer = q(equation)
    if answer[0] > 0:
        return answer[0]
    else:
        return answer[1]
    
###########################################################################
# Functions for Problem 7
###########################################################################
#INPUT parameters to LV model
#OUTPUT two lists history_rabbit, history_fox of populations
def rabbit_fox(br,dr,df,bf,rabbit,fox,time_limit):
    i = 0
    history_rabbit = []
    history_fox = []
    while i < time_limit:
        history_rabbit.append(rabbit)
        history_fox.append(fox)
        i += 1
        rtemp = rabbit
        rabbit = math.ceil(rabbit + (rabbit*br) - (rabbit*fox*dr))
        fox = math.ceil(fox + (bf*dr*rtemp*fox) - (fox*df))
    return history_rabbit, history_fox




###########################################################################
# Functions for Problem 8
###########################################################################
# INPUT container, sample size n
# OUTPUT random selection of size n in any order
# CONSTRAINT uses random 
# This is with replacement
def sub_strings(str,cnt):
    length = len(str)
    i = 0
    j = 1
    tmp = ""
    while i < length:
        count = 0
        while j < length + 1:
            tmp = str[i:j]
            k = 0
            if not tmp in cnt:
                while k+j < length + 1:
                    hold = str[i+k:j+k]
                    if hold == tmp:
                        count += 1
                    k += 1 
                cnt[tmp] = count
                count = 0
            j += 1
        i += 1
        j = i+1    
    return cnt


###########################################################################
# Functions for Problem 9
###########################################################################
#INPUT values for annuity
#OUTPUT deposit amount needed
def deposit(S,i,n):
    return -(S/(i*math.pow(1+i,n)-i))


#INPUT sinking fund values except deposit
#OUTPUT a list of period, deposit, interest, accrued total fund
def sinking_fund(final_amt, r, m, y):
    i = r/m
    n = m*y
    S = final_amt
    R = deposit(S,i,n)




###########################################################################
# Functions for Problem 10
###########################################################################
#INPUT list of numbers
#OUTPUT Boolean if geometric series
def is_geometric_sequence(lst):
    temp = lst[1]/lst[0]
    k = 1
    while k < len(lst) - 1:
        new = lst[k+1]/lst[k]
        if new == temp:
            temp = new
            k += 1
        else:
            return False
    return True



###########################################################################
# Functions for Problem 11
###########################################################################
#INPUT portfolio of stock price, shares, market
#OUTPUT current total value
def value(portfolio, market):
    start_value = 0
    end_value = 0
    for i in portfolio['stock']:
        start_value += portfolio['stock'][i][1]*portfolio['stock'][i][0]
        end_value += portfolio['stock'][i][1]*market[i]
    return round((end_value - start_value)/start_value*100,0)



if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here
    """

    #problem 1
    # print(day([14,2,2000]))
    # print(day([14,2,1963]))
    # print(day([14,2,1972]))

    # #problem 2
    # print(q((3,4,2)))
    # print(q((1,3,-4)))
    # print(q((1,-2,-4)))

    # #problem 3
    # people0 = [[0,1,1],[1,0,0],[1,1,1]]
    # print(match(people0))
    # print(best_match(match(people0)))

    # people1 = [[0,1,1,0,0,0,1],
    #            [1,1,0,1,1,1,0],
    #            [1,0,1,1,0,1,1],
    #            [1,0,0,1,1,0,0],
    #            [1,1,1,0,0,1,0]]
    # print(best_match(match(people1)))
    # output is ([1, 1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 0, 0], 39.23)

    # v0,v1 = (2,3,-1), (1,-3,5)
    # print(angle(v0,v1)) #122.83

    # v0,v1 = (3,4,-1),(2,-1,1)
    # print(angle(v0,v1)) #85.41

    # v0,v1 = (5,-1,1),(1,1,-1)
    # print(angle(v0,v1)) #70.53


    # #problem 4 pairs should be identical
    # print(q((1,-4,-8)), q_((1,-4,-8)))
    # print(q((1,3,-4)),q_((1,3,-4)))
   
    
    # #problem 5
    # lst = [1,3,3,2,9,10]

    # print(mean(lst))
    # print(var(lst))
    # print(std(lst))
    # print(mean(mean_centered(lst)))

    # #problem 6
    # s = (-.025,-.5,60)
    # d = (0.02,.6,20)
    # print(equi(s,d))
    
    # s = (5,7,-350)
    # d = (4,-8,1000)

    # print(equi(s,d))

    #problem 7
    # br = 0.03
    # dr = 0.0004
    # df = 0.25
    # bf = 0.11
    # rabbit = 3000  #initial population size
    # fox = 200  #initial population size
    # time_limit = 2000
    # history_rabbit, history_fox = rabbit_fox(br,dr,df,bf,rabbit,fox, time_limit)

    # #uncomment to see time, rabbit, fox populations
    # for j in range(0,2000,200):
    #     print(j, history_rabbit[j], history_fox[j])


    # plt.plot(list(range(0,time_limit)),history_rabbit)
    # plt.plot(list(range(0,time_limit)),history_fox)
    # plt.xlabel("Time")
    # plt.ylabel("Population Size")
    # plt.legend(["Rabbit","Fox"])
    # plt.title("Lotka-Volterra Model for Rabbit & Fox")
    # plt.show()

    
    # #problem 8
    # data = ["abcabc","ccccc",""]
    # # data = ["abcabc"]
    # for d in data:
    #     cnt = {}
    #     sub_strings(d,cnt)
    #     print(cnt)

    # #problem 9
    # S = 30000
    # m = 4
    # r = 10/100
    # y = 2
    # for i in sinking_fund(S,r,m,y):
    #     print(i)


    #problem 10
    # data = [[1,2,4,6],[2,4,8,16],[10,30,90,270,810,2430]]
    # for d in data:
    #     print(is_geometric_sequence(d))


    #problem 11
    portfolios =  {'A':{'stock':{'x':(41.45,45),'y':(22.20,1000)}},
    'B':{'stock':{'x':(33.45,15),'y':(12.20,400)}}}
    market = {'x':43.00, 'y':22.50}


    for name, portfolio in portfolios.items():
        print(f"{name} {value(portfolio,market)}")
