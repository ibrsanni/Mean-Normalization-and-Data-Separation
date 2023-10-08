## MEAN NORMALIZATION
### TO DO:
1. You will start by importing NumPy and creating a rank 2 ndarray of random integers between 0 and 5,000 (inclusive) with 1000 rows and 20 columns. This array will simulate a dataset with a wide range of values. Fill in the code below
   
2. Now that you created the array we will mean normalize it. We will perform mean normalization using the following equation:            
Norm_Col𝑖 = Col𝑖−𝜇𝑖/𝜎𝑖
where:  
   * Col𝑖 is the 𝑖th column of  𝑋
   * 𝜇𝑖 is average of the values in the  𝑖th column of  𝑋 
   * 𝜎𝑖 is the standard deviation of the values in the  𝑖th column of 𝑋.
 
In other words, mean normalization is performed by subtracting from each column of  𝑋 the average of its values, and then by dividing by the standard deviation of its values. Below, you will first calculate the average and standard deviation of each column of  𝑋.

1. If you have done the above calculations correctly, then ave_cols and std_cols, should both be vectors with shape (20,) since  𝑋 has 20 columns.
   
2. You can now take advantage of Broadcasting to calculate the mean normalized version of  𝑋 in just one line of code using the equation above.
   
3. If you have performed the mean normalization correctly, then the average of all the elements in  𝑋norm should be close to zero, and they should be evenly distributed in some small interval around zero. 

## DATA SEPARATION
### TO DO:
1. In the space below create a rank 1 ndarray that contains a random permutation of the row indices of X_norm. You can do this in one line of code by extracting the number of rows of X_norm using the shape attribute and then passing it to the np.random.permutation() function. Remember the shape attribute returns a tuple with two numbers in the form (rows,columns)
   
2. Now you can create the three datasets using the row_indices ndarray to select the rows that will go into each dataset. Rememeber that the Training Set contains 60% of the data, the Cross Validation Set contains 20% of the data, and the Test Set contains 20% of the data. Each set requires just one line of code to create. 
   
3. If you performed the above calculations correctly, then X_tain should have 600 rows and 20 columns, X_crossVal should have 200 rows and 20 columns, and X_test should have 200 rows and 20 columns.