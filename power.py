def singledigit(d):
    if len(d) == 0:
        return ""
    if int(d) == 0:
        return "zero"
    elif int(d) == 1:
        return "one"
    elif int(d) == 2:
        return "two"
    elif int(d) == 3:
        return "three"
    elif int(d) == 4:
        return "four"
    elif int(d) == 5:
        return "five"
    elif int(d) == 6:
        return "six"
    elif int(d) == 7:
        return "seven"
    elif int(d) == 8:
        return "eight"
    elif int(d) == 9:
        return "nine"
        
def teens(d):
    if d == "":
        return "ten"
    elif int(d) == 1:
        return "eleven"
    elif int(d) == 2:
        return "twelve"
    elif int(d) == 3:
        return "thirteen"
    elif int(d) == 4:
        return "fourteen"
    elif int(d) == 5:
        return "fifteen"
    elif int(d) == 6:
        return "sixteen"
    elif int(d) == 7:
        return "seventeen"
    elif int(d) == 8:
        return "eighteen"
    elif int(d) == 9:
        return "nineteen"

def tens(a, b):
    ret = ""
    if b == "0":
        b = ""
    if int(a) == 1:
        return teens(b)
    elif int(a) == 2:
        ret = "twenty " + singledigit(b)
    elif int(a) == 3:
        ret =  "thirty " + singledigit(b)
    elif int(a) == 4:
        ret =  "fourty " + singledigit(b)
    elif int(a) == 5:
        ret =  "fifty " + singledigit(b)
    elif int(a) == 6:
        ret =  "sixty " + singledigit(b)
    elif int(a) == 7:
        ret =  "seventy " + singledigit(b)
    elif int(a) == 8:
        ret =  "eighty " + singledigit(b)
    elif int(a) == 9:
        ret =  "ninety " + singledigit(b)
    
    if b =="":
        return ret[:-1]
    else:
        return ret

def wordify(n):
    if len(str(n)) == 1:
        return singledigit(str(n))
    elif len(str(n)) == 2:
        val = list(str(n))
        return tens(val[0], val[1])
    elif len(str(n)) == 3:
        val = list(str(n))
        if (int(val[1]) > 0):
            return "{} hundred {}".format(singledigit(val[0]), tens(val[1], val[2]))
        elif int(val[1]) == 0 and int(val[2]) > 0:
            return "{} hundred {}".format(singledigit(val[0]), singledigit(val[2]))
        else:
            return "{} hundred".format(singledigit(val[0]))
     
def main():
	print wordify(10)
	print wordify(1)
	print wordify(7)
	print wordify(17)
	print wordify(25)
	print wordify(325)
	print wordify(100)
	print wordify(146)
	

if __name__=="__main__":
	main()
