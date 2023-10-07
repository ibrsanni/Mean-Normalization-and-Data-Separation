# import numpy into pythom
import numpy as np

# Create a 1000 x 20 ndarray with random integers in the half-open interval [0, 5001).
X = np.random.randint(0, 5001, size = (1000, 20))

# print the shape of X
print('X: ', X.shape)

# Average of the values in each column of X
ave_cols = np.mean(X, axis = 0)
print(ave_cols)

# Standard Deviation of the values in each column of X
std_cols = np.std(X, axis = 0)
print(std_cols)

# Print the shape of ave_cols
print(ave_cols.shape)

# Print the shape of std_cols
print(std_cols.shape)

# Mean normalize X
X_no = X - ave_cols
X_norm = X_no / std_cols

# Print the average of all the values of X_norm
avg_Xnorm = np.mean(X_norm)
print(avg_Xnorm)

# Print the average of the minimum value in each column of X_norm
min_avg = np.min(X_norm, axis = 0)
print(min_avg)

avg_mean_min = np.mean(min_avg)
print(avg_mean_min)

# Print the average of the maximum value in each column of X_norm
max_avg = np.max(X_norm, axis = 0)
print(max_avg)

avg_mean_max = np.mean(max_avg)
print(avg_mean_max)

# We create a random permutation of integers 0 to 4
np.random.permutation(5)

# Create a rank 1 ndarray that contains a random permutation of the row indices of `X_norm`
print(X_norm.shape)
row_indices = np.random.permutation(X_norm.shape[0])
print(row_indices)

# Make any necessary calculations.
num_rows = row_indices.shape[0]
train = int(0.6 * num_rows)
crossval = int(0.2 * num_rows)
test = num_rows - train - crossval


# You can save your calculations into variables to use later.
X_train, X_crossVal, X_test = np.split(row_indices, [train, train + crossval])

# Create the actual sets using the row indices

# Create a Training Set
X_train = X_norm[X_train]

# Create a Cross Validation Set
X_crossVal = X_norm[X_crossVal]

# Create a Test Set
X_test = X_norm[X_test]

# Print the shape of X_train
print(X_train.shape)

# Print the shape of X_crossVal
print(X_crossVal.shape)

# Print the shape of X_test
print(X_test.shape)