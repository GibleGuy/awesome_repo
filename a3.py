import math

#Problem 1

#INPUT n0 start colony size, m growth rate, t time
#RETURN final colony size
def N(n_0, m, t):
    return n_0*math.exp(m*t)

#INPUT t days
#RETURN number of teeth
def N_t(t):
    return math.ceil(71.8*math.exp(-8.96*math.exp(-0.0685*t)))


#INPUT pressures Pi, Pf 
#RETURN work joules
def W(P_i, P_f):
    return math.ceil(8.314*300*math.log(P_i/P_f, math.e))


#INPUT V miles per hour, A area, C_l lift coefficient
#RETURN lbs 
def L(V,A,C_l):
    return math.ceil(0.0033*(V*V)*A*C_l)

###########################################################################
# Functions for Problem 2
###########################################################################
#INPUT coef = (a,b,c)
#RETURN tuple ('up'|'down', (vertex, y-value of vertex))
###########################################################################
def q(coef):
    a,b,c = coef

    if a > 0:
        open = 'up'
    else:
        open = 'down'
    
    x = -b/(2*a)
    y = a*(x*x)+b*x+c
    return (open, (round(x, 2), round(y, 2)))



###########################################################################
# Functions for Problem 3
###########################################################################
#INPUT object x and list lst
#RETURN True if object occurs in the list
#CONSTRAINT You cannot use 'x in y' -- must use bounded looping
def m(x,lst):
    checker = False
    for item in lst:
        if x == item:
            checker = True
    return checker

#INPUT receipt= [[x0,y0],[x1,y1],...,[xn,yn]]
# x is item, y is cost
# tax_rate is the tax on taxable items
# no_tax is a list of items not taxable
#RETURN total amount owed (round values to 2 nearest decimal places)
def amt(reciept, tax_rate, no_tax):
    total = 0
    for x in reciept:
        if m(x[0], no_tax):
            total += x[1]
        else:
            total += x[1]*(1+tax_rate)
    return round(total, 2)



###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT p0 = (x0,y0) p1 = (x1,y1)
#RETURN dictionary y = mx + b
def make_line(p0,p1):
    x0,y0,x1,y1 = *p0,*p1
    m = round((y1 - y0)/(x1 - x0),2)
    b = round(y0 - (m*x0),2)
    return {'m':m, 'b':b}

#INPUT two lines as dictionary
#RETURN a point (x,y) of intersection or "same line", "parallel lines" 
#rounded to two places
def intersection(l0,l1): 
    if l0['m'] == l1['m']:
        if l0['b'] == l1['b']:
            return "same line"
        else:
            return "parallel lines"
    else:
        x = round((l0["b"] - l1['b'])/(l1['m'] - l0['m']), 2)
        y = round(l1['m'] * x + l1['b'],2)
        return (x,y)

        


###########################################################################
# Functions for Problem 5
###########################################################################
#INPUT List of numbers
#RETURN Various means or error message

def arithmetic_mean(nlst):
    if not nlst:
        return "Data Error: 0 values"
    y = 0
    n = 0
    for x in nlst:
        n += 1
        y += x
    return y/n 

def geo_mean(nlst):
    if not nlst:
        return "Data Error: 0 values"
    sum = 0
    n = 0
    for x in nlst:
        sum += math.log10(x)
        n += 1
    return math.pow(10, sum/n)


def har_mean(nlst):
    if not nlst:
        return "Data Error: 0 values"
    n = 0
    sum = 0
    for x in nlst:
        if x == 0:
            return "Data Error: 0 values"
        n += 1
        sum += 1/x
    return n/sum

def RMS_mean(nlst):
    if not nlst:
        return "Data Error: 0 values"
    n = 0
    sum = 0
    for x in nlst:
        sum += x*x
        n += 1
    return math.sqrt(sum/n)

###########################################################################
# Function for Problem 6
###########################################################################
#INPUT x object, list of objects, integer y
#RETURN true if x occurs at least y times, false otherwise
def occur_at_least(x,y,lst):
    n = 0
    for item in lst:
        if item == x:
            n += 1
            if n == y:
                return True
    else:
        return False



###########################################################################
# Functions for Problem 7
###########################################################################
#input two objects x,y and list
#returns True if x occurs strictly more than y in lst, False otherwise
def occurs_more(x,y,lst):
    if not lst:
        return True
    count_x = 0
    count_y = 0
    for item in lst:
        if item == x:
            count_x += 1
        if item == y:
            count_y += 1
    if count_x > count_y:
        return True
    else:
        return False 




#input two objects x, y and list
#return if the number of times x,y occur in list are equal, then return the list
#if x occurs more than y, then remove the occurrences from the left side until
#their counts are equal, then return the list
#if y occurs more than x, the same procedure
def equal_remove(x,y,lst):
    while True:
        if occurs_more(x, y, lst):
            lst.remove(x)
        elif occurs_more(y, x, lst):
            lst.remove(y)
        else:
            return lst

###########################################################################
# Functions for Problem 8
###########################################################################
#INPUT list of numbers
#RETURN True if geometric series, False otherwise
def is_geo(xlst):
    if len(xlst) <= 2:
        return 0
    
    placeholder = xlst[1]/xlst[0]
    count = 2
    while count+1 <= len(xlst):
        if not (xlst[count]/xlst[count-1]) == placeholder:
            return 0
        else:
            placeholder = xlst[count]/xlst[count-1]
            count += 1
    return 1


###########################################################################
# Functions for Problem 9
###########################################################################
#INPUT pair of points in 2D
#RETURN distance round to two decimal places
def net_displacement(p0,p1):
    return round(math.pow(math.pow(p0[0]-p1[0],2) + math.pow(p0[1]-p1[1], 2), 1/2), 2)

#INPUT starting position (x,y) and list of one step directions w,e,s,n that move the positon
#of x,y
#RETURN a tuple final destination, distance, distance from start
def track(start_pos, movement):
        x, y = start_pos
        dist = 0
        for coord in movement:
            if coord == 'e':
                x += 1
            if coord == 'w':
                x -= 1
            if coord == 's':
                y -= 1
            if coord == 'n':
                y += 1
            dist += 1
        return ((x,y), dist, net_displacement(start_pos, (x,y)))


###########################################################################
# Functions for Problem 10
###########################################################################
#INPUT pair of tuples from tracking
#RETURN distance betweem two ending places 
def final_distance(m0,m1):
    return net_displacement(m0[0], m1[0])



###########################################################################
# Functions for Problem 11
###########################################################################
#INPUT conference and game
#RETURN the dictionary conference after changing wins,losses, percentages of teams (there are no ties)
def update(conference, game):
    win_key = 'frogs'
    loss_key = 'chickens'
    temp = 0
    team_names = game.keys()
    for x in team_names:
        if game[x] > temp:
            temp = game[x]
            loss_key = win_key
            win_key = x
        else:
            loss_key = x

    conference[win_key]['W'] += 1
    conference[loss_key]['L'] += 1
    conference[win_key]['PCT'] = round(conference[win_key]['W']/(conference[win_key]['W'] + conference[win_key]['L']), 3)
    conference[loss_key]['PCT'] = round(conference[loss_key]['W']/(conference[loss_key]['W'] + conference[loss_key]['L']), 3)

    return conference



###########################################################################
# Functions for Problem 12
###########################################################################
#INPUT amt and list of donations
#RETURN tuple: amt, donations left, the amount of the goal left
def go_fund_me(amt, donations):
    my_sum = -(amt)
    while my_sum < 0:
        if not donations:
            break
        my_sum += donations[0]
        donations = donations[1:]
    return (amt, donations, my_sum)


###########################################################################
# Functions for Problem 13
###########################################################################
#INPUT credit score cr and list of potential clients [[n0,cd0],[n1,cd1],...,[nm,cdm]] where n is name, cd is unweighted dictionary of credit values
#RETURN list of people and their score that is strictly greater than cr; if nobody qualifies, then return empty list
def loan(cr, lst):
    score = 0
    returnees = []
    for x in lst:
        values = x[1]
        score = (values["P"]*0.35) + (values["A"]*0.3) + (values['L']*0.15) + (values['N']*0.1) + (values['C']*0.1)
        if score > cr:
            returnees += [[x[0], score]]
    return(returnees)

#Problem 14
#INPUT current temperature T(t) of fish (T_t, environment T_e, temperature of fish and lst of what dogs were doing hours ago]
#OUTPUT The time (in hours) that elapsed after the murder reported as a float
#you must determine k from problem and formula from description
def time(T_t, T_e, T_0):
    #k = ??? #you have to determine this
    k = 0.287682
    return math.log((T_t-T_e)/(T_0-T_e), math.e)/-k

if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here
    """
    # #problem 1
    # print(N(500,100,4)) 
    # print(N_t(1000))
    # print(W(10,1))
    # print(L(33.8,512,0.515))

    #problem 2
    # print(q((-2.6,7.6,-10)))
    # print(q((1,-10.2,26.01)))

    #problem 3
    # receipt = [[1,1.45],[3,10.00],[2,1.45],[5,2.00]]
    # tax_rate,no_tax = 7/100, [33,5,2]
    # print(amt(receipt,tax_rate, no_tax))
    # print(amt(receipt,10/100,[]))

    # #problem 4
    # p0 = (32,32)
    # p1 = (29,5)
    # p2 = (15,10)
    # p3 = (49,25)
    # p4 = (15,30)
    # p5 = (50,15)
 
    # l0,l1 = make_line(p0,p1),make_line(p2,p3)
    # print(intersection(l0,l1))
    # l0 = make_line(p4,p5)
    # print(intersection(l0,l1))
    
    # p6,p7,p8 = (0,0),(1,1),(2,2)
    # p9,p10 = (0,1),(1,2)
    # print(intersection(make_line(p6,p7),make_line(p7,p8))) # same line
    # print(intersection(make_line(p6,p7),make_line(p9,p10))) # parallel lines

    #problem 5
    # print(arithmetic_mean([1,2,3]))
    # print(geo_mean([2,4,8]))
    # print(har_mean([1,2,3]))
    # print(RMS_mean([1,3,4,5,7]))

    #problem 6
    # data = [[1,4,[1,2,1,2,1,1]], [1,3,[1,2,1,2,1,1]], [1, 4, [1,2,1,2,1,0]], ]

    # for d in data:
    #     print(occur_at_least(*d))

    #problem 7
    # lst = [2,2,3,1,2,1,1,2]
    # print(occurs_more(1,2,lst))
    # print(occurs_more(2,3,lst))
    # print(occurs_more(2,3,[]))
    # print(equal_remove(1,2,lst))
    # print(equal_remove(1,3,lst))
    # print(equal_remove(2,3,lst))
    # print(occurs_more(2,3,(equal_remove(2,3,lst))))

    # #problem 8
    # xlst = [1/2,1/4,1/8,1/16,1/32]
    # print(is_geo(xlst))
    # xlst = [1,-3,9,-27]
    # print(is_geo(xlst))
    # xlst = [625,125,25]
    # print(is_geo(xlst))
    # xlst = [1/2,1/4,1/8,1/16,1/31]
    # print(is_geo(xlst))
    # xlst = [1,-3,9,-26]
    # print(is_geo(xlst))
    # xlst = [625,125,24]
    # print(is_geo(xlst))
    # print(is_geo([1/2,1/4]))

    # #problem 9
    # data_m9 = [[(0,0), list(10*'n' + 15*'e' + 10*'s'+15*'w')],
    #       [(0,0), list(3*'n' + 4*'e')],
    #       [(1,2), list(3*'s' + 4*'w')]]

    # for d in data_m9:
    #     print(track(*d))
    # e = "e"
    # n = "n"
    # s = "s"
    # w = "w"
    # print(track((9,7),['e','e',s,'e',w,w,w,n,s,w,s,w,w,'e','e','e',s,w,s,'e',n,'e','e',n,s,n,n,s,'e','e',n,n]))
    
    
    # #problem 10
    # data_m10 = [[(0,0), list(10*'n' + 15*'e' + 10*'s'+15*'w')],
    #       [(0,0), list(3*'n' + 4*'e')],
    #       [(1,2), list(3*'s' + 4*'w')]]

    # print(final_distance(track(*data_m10[1]),track(*(data_m10[2]))))

    # #problem 11
    # big_10_women = {'IU':{'W':12,'L':1,'PCT':.923, 'Home':(13,0)},
    #             'PU':{'W':6,'L':6,'PCT':.500, 'Home':(8,4)}, 
    #             'IOWA':{'W':11,'L':1,'PCT':.917, 'Home':(11,1)},
    #             'NW':{'W':1,'L':11,'PCT':.083,'Home':(6,6)}}
    
    # print(big_10_women['IU'],big_10_women['IOWA'])
    # update(big_10_women,{'IU':87,'IOWA':78})
    # print(big_10_women['IU'],big_10_women['IOWA'])
    
    # update(big_10_women, {'IU':8,'IOWA':7})
    # print(big_10_women)
    
    # update(big_10_women, {'PU':87,'NW':91})
    # print(big_10_women)
    
    # update(big_10_women, {'IOWA':89,'PU':75})
    # print(big_10_women)
    

    # #problem 12
    # data12 = [[100,[10,15,20,30,29,13,15,40]],
    #     [100,[]],
    #     [100,[30,4]]]

    # for d in data12:
    #     print(go_fund_me(*d))
    # print(go_fund_me(50, [45,47,78]))

    #Problem 13
    # data = [['x',{'P':600, 'L':700,'A': 500, 'N': 170, 'C': 250}],
    #     ['y',{'P':550, 'L':720,'A': 500, 'N': 230, 'C': 250}],
    #     ['b',{'P':560, 'L':710,'A': 500, 'N': 221, 'C': 250}],
    #     ['c',{'P':800, 'L':700,'A': 200, 'N': 100, 'C': 150}],
    #     ['a',{'P':800, 'L':800,'A': 600, 'N': 250, 'C': 150}],
    #     ['z',{'P':800, 'L':800,'A': 500, 'N': 250, 'C': 150}]]
    # print(loan(550,data))

    #problem 14
    #initial scene of the crime data
   
    no_alibis = {"Ursala":[3,4],"Shilah":[2,2.5],"Kaiser":[1,2]}
    T_t = 81
    T_e = 65
    T_0 = 85
    time_discovered = 4 #PM Dr. D's living room
    suspects = []

    time_of_murder = time_discovered - time(T_t, T_e, T_0)
    for name,times in no_alibis.items():
        start,end = times
        if start <= time_of_murder <= end:
            suspects.append(name)
    print(f"The suspect(s) {suspects}")