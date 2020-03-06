def count_to(count):
    numbers_in_chinese = ["yi", "er", "san", "si", "wu", "liu", "qi", "ba"]

    iterator = zip(range(count), numbers_in_chinese)

    for pos, num in iterator:
        yield num


for i in count_to(int(input("Enter the number to which you wish to count in Chinese: "))):
    print(i)
