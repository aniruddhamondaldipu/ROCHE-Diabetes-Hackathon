stats={}
def fizzbuzz(*args):
        result = []
        for i in range(1, l + 1):
            a = i % int1 == 0
            b = i % int2 == 0

            if a and b:
                result.append(str1 + str2)
            elif a:
                result.append(str1)
            elif b:
                result.append(str2)
            else:
                result.append(str(i))

        key = (int1, int2, l, str1, str2)
        stats[key] = stats.get(key, 0) + 1

        return result

def get_statistics():
    max_hits = max(stats.values(), default=0)

    most_used_inputs = [
        (*key, hits) for key, hits in stats.items() if hits == max_hits
    ]
    if most_used_inputs is not None:
        

        result = {
            "Most Used Input": [
                {
                "Fizz Value : ": int1,
                "Buzz Value : ": int2,
                "Lenth Of List : ": l,
                "Word 1 : ": str1,
                "Word 2 : ": str2,
                "Hits": hits
                } for int1, int2, l, str1, str2, hits in most_used_inputs
            ]
        }
        return result
    else:
        return {"message": "No statistics available"}


n=input("Please enter number of time wanted to provide input : ")
for i in range(int(n)):
    print("Please Enter the Input Value")
    
    int1 = int(input("Fizz Value : "))
    int2 = int(input("Buzz Value : "))
    l = int(input("Lenth Of List : "))
    str1 = str(input("Word 1 : "))
    str2 = str(input("Word 2 : "))
    print(fizzbuzz(int1,int2,l,str1,str2))
print("Statistics : \n",get_statistics())