# importing library
import numpy 

def set_array(L,rows,cols):
    ans=numpy.array(L).reshape(rows,cols)
    return ans


# initializing list
lst = [1, 7, 0, 6, 2, 5, 6, 8]

# converting list to array
arr = set_array(lst,2,4)



# displaying list
print ("List: ", lst)

# displaying array
print ("Array: ", arr)
