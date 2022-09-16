def hello():
    print("Hello there!")

def pack(sandwich, juicebox, apple):
    return ["sandwich", "juicebox", "apple"]

def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"First I eat {list[0]}")
            else:
                print(f"Next I eat {list[i]}")


hello()
print(pack("sandwich", "juicebox", "apple"))
eat_lunch(["sandwich", "juicebox", "apple"])