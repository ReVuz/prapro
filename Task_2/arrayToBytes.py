import numpy as np
import time

#Creating a numpy array

start_time = time.time()
arr = np.random.randint(0, 10, size=(1000, 1000))
end_time = time.time()
print(f'Original Array : \n{arr}\n\nShape of array : {arr.shape}')
print(f"\nCreating the Original array took {end_time - start_time} seconds.")

#Converting the array to bytes
arr_bytes = arr.tobytes()
print("\nArray converted to bytes")

# print(f'\nStart Time : {start_time}\t\tEnde Time : {end_time}')
# print(f'\nConverting the array to bytes took {end_time - start_time} seconds.')

#Recreating the Array
new_array = np.frombuffer(arr_bytes,dtype=arr.dtype)
# print(f'\nRecreated array : \n{new_array}\n\nShape : {new_array.shape}')

# Verify if the recreated array is similar to the original array
if(np.array_equal(arr,new_array)) :
    print("Recreated array is equal to the Original array")
else : 
    new_array = new_array.reshape(1000,1000)
    print(f'\nRecreated array : \n{new_array}\n\nShape : {new_array.shape}')
    
# print(np.array_equal(arr,new_array))