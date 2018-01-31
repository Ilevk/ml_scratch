import numpy as np


def n_size_ndarray_creation(n, dtype=np.int):
    return np.arange(n*n).reshape(n,n)


def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int):
    if type == 0:
        return np.zeros(shape,dtype)
    elif type == 1:
        return np.ones(shape,dtype)
    else:
        return np.empty(shape,dtype)


def change_shape_of_ndarray(X, n_row):
    if n_row == 1:
        return np.array(X).flatten()
    else:
        return np.array(X).reshape(n_row,-1)


def concat_ndarray(X_1, X_2, axis):
    if X_1.ndim == 1 :
        X_1 = np.array(X_1).reshape(1,-1)
    if X_2.ndim == 1 :
        X_2 = np.array(X_2).reshape(1,-1)
        
    a = X_1.shape
    b = X_2.shape
        
    if axis == 0:
        if a[1] == b[1]:
            return np.concatenate((X_1,X_2),axis)
        else :
            return False
    elif axis == 1:
        if a[0] == b[0]:
            return np.concatenate((X_1,X_2),axis)
        else :
            return False 


def normalize_ndarray(X, axis=99, dtype=np.float32):
    if axis == 99:
        mean = X.mean()
        std = X.std()
        x = (X - mean)/std
    else :
        mean = X.mean(axis)
        std = X.std(axis)
        
        if axis == 0:
            x = (X - mean.T)/std.T
        else:        
            x = (X.T - mean)/std
            x = x.T
            
    return x


def save_ndarray(X, filename="test.npy"):
    np.save(filename,arr=X)


def boolean_index(X, condition):
    
    a = np.where(eval(str("X")+condition))
    return a


def find_nearest_value(X, target_value):
    a = X-target_value
    a = np.abs(a)
    result = np.argmin(a)
    return X[result]


def get_n_largest_values(X, n):
    result = np.arange(n, dtype = np.float32)
    index = np.arange(n,dtype = int)
    for i in range(n):
        a = np.argmax(X)
        result[i] = X[a]
        index[i] = a
        X[a] = 0
    for i in range(n):
        X[index[i]] = result[i]
    return X[index]