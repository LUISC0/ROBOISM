def duplicate(x):
    for i in range(0, len(x)):
        for j in range(i + 1, len(x)):
            if (x[i] == x[j]):
                print(x[j]);

var = input("Enter a array of numbers:")
duplicate(var)
