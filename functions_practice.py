def hello():
    print("Hello!")

def pack(a, b, c):
    return [a, b, c]

def eat_lunch(food_list):
    if len(food_list) == 0:
        print("Lunch be empty, yo")
    else:
        for i in range(len(food_list)):
            if i == 0:
                print(f"First I eat {food_list[0]}")
            else:
                print(f"Next I eat {food_list[i]}")

# Went to solutions file for calling these, wasn't sure exactly how you wanted them to be called.
                
hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["granola bar","bagel","sandwich","donut"])