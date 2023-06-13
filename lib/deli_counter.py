katz_deli = ['ada','bada','cada','dada']

def line(line):
    linestr = "The line is currently:"
    if line == []:
        print("The line is currently empty.")
        return "The line is currently empty."
    else:
        i = 0
        for val in line:
            linestr = f"{linestr} {i+1}. {val}"
            i+=1
        print(linestr)
        return linestr

    
def take_a_number(deli,name):
    #append the name to the list and then list get the idx that is added
    spot = len(deli)+1
    deli.append(name)
    print(f"Welcome, {name}. You are number {spot} in line.")
    return (f"Welcome, {name}. You are number {spot} in line.")
    

def now_serving(deli):
    if deli == []:
        print("There is nobody waiting to be served!")
    else:
        out = deli.pop(0)
        print(f"Currently serving {out}.")
    return 1

line(katz_deli)  




