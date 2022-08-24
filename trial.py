# The input is an array of integers
# The process- check for the dominating interger(If the common interger appears more than the length of the array, prints the index of the dominant else prints -1 )
# We have the keys and the values in the array.
# IN order to check for the most dominant integer, we have to loop through the array and use (in), also check for the occurences using count
# if the length(A)>count(A);
# The output is one interger in the array that is most dominant.

def checkOccurrences(A):
    # creating an empty dictionary that will store the list of occurences
    elements={}
    # looping through the array 
    for x in A:
    # creating aconditional statement that will check for the presence of the keys in the dictionary
        if x in elements.keys():
            elements[x] +=1
        else:
            elements[x] = 1
    # printing the list of occurences in a dictionary
    print(elements)
#    checking for the most dominant elemement in the dictionary using an inbuilt function.
    common_num=[(value,key) for key,value in elements.items()]
    # displaying the most dominant key in the dictionary.
    most_common=max(common_num)[1]
    print(max(most_common))  
# finding the length of the elemnts in the dictionary.
    length_elements=len(elements)
    print(length_elements)

    # if length_elements>most_common:
    #     print(x)
    # else:
    #     print("-1")


checkOccurrences([1,2,3,3,4,4,4,5,1,6])

