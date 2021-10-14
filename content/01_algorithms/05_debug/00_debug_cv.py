import numpy as np
import random

def synthetic_classification(n_samples=10, n_features=1, shuffle=False, 
                             random_seed=None):
    '''
    Generates a simple random synthetic dataset in a given shape.
    Used for testing of generator classes.
    
    X: each feature is a sequence i to i + n_samples where i is the feature no.
    y data is 0 or 1 weighted very roughly 50/50.
    
    These sequences are randomised if shuffle is set to True.
    
    No error checking. Assumes all inputs are valid.
    
    Params:
    ------
    n_samples: int, optional (default=10)
        The number of samples
        
    n_features: int, optional (default=1)
        The number of features in the classification problem
        
    shuffle: bool, optional (default=False)
        If true then sequences are randomly shuffled
        
    random_seed: int or None, optional (default=None)
        If shuffle then controls the ordering of the sequences generated.
    
    Returns:
    --------
    X, y
    Where X and y are np.ndarrays and X will have shape 
    (n_samples, n_features) 
        
    '''
    X = [[(col * (n_samples)) + row for col in range(n_features)] 
                                          for row in range(n_samples)]
    y = ([1] * (n_samples // 2)) + ([0] * ((n_samples // 2) + (n_samples % 2)))
    
    if shuffle: 
        for lst in [X, y]:
            random.seed(random_seed)
            random.shuffle(lst)
    return np.array(X), np.array(y)


class KFold:
    '''
    K-fold cross validation of a X, y formatted dataset.
    Optional random shuffling of input data.
    Note that original data is not shuffled, but a copy of a shuffled
    array is created.
    '''
    def __init__(self, k=5, shuffle=False, random_seed=None):
        '''
        Params:
        -------
        k: int
            The number of folds
            
        shuffle: bool, optional (default=False)
            When True the data are randomly shuffled
            
        random_seed: int or None, optional (default=None)
            When shuffle set to true and random_seed is an integer the shuffling
            of the dataset is controlled prior to folding.
        '''
        self.k = k
        self.shuffle = shuffle
        self.rng = np.random.default_rng(random_seed)
    
    def __repr__(self):
        rep = f'KFoldCV(k={self.k}, shuffle={self.shuffle},' \
                + f'random_seed={self.random_seed})'


    def get_n_splits(self, X):
        '''
        Return an integer representing the number of splits that 
        will be generated.
    
        '''
        return self.k

    def split(self, X, y):
        '''
        Generator method.  Returns incremental splits of the dataset
        on each call.
        
        Params:
        ------
        X: array-like 
            python list or numpy.ndarray containing X data. For multiple features
            shape should be (n_samples, n_features)
        
        y: array-like
            python list or numpy.ndarray containing y target data. For multiple 
            targets shape should be (n_samples, n_targets)
        
        Returns:
        --------
        train_X, test_X, train_y, test_y 
        
        Where each is a np.ndarray
        '''
        # convert lists to numpy arrays
        X, y = np.asarray(X), np.asarray(y)
        
        # store the indexes of each element - its these that get shuffled.
        if self.shuffle:
            idx = self.rng.integers(0, len(X), size=len(X))
        else:
            idx = np.arange(len(X), dtype=np.int16)
        
        # length of k - 1 splits... final split continues to end.
        split_len = int(len(X) / (self.k))

        for test_idx in range(0, len(X), split_len):
        
            # create k - 1 training folds for X 
            train_X = self._fold_training_data(X, idx, test_idx, split_len)
            # X test data for fold
            test_X = X[idx[test_idx: test_idx+split_len]]
            
            # create k - 1 training segments for y
            train_y = self._fold_training_data(y, idx, test_idx, split_len)
            # y test data fold
            test_y = y[idx[test_idx: test_idx+split_len]]
            
            yield train_X, test_X, train_y, test_y
            
        
    def _fold_training_data(self, data, idx, test_idx, split_len):
        '''
        create training segments for X or y
        '''
        train_seg1 = data[idx[:test_idx]]
        train_seg2 = data[idx[test_idx + split_len: ]]                              
        return np.concatenate([train_seg1, train_seg2])


if __name__ == '__main__':
    # generate test dataset
    X, y = synthetic_classification(n_samples=10, n_features=1, shuffle=False)

    # create an instance of LeaveNOut
    cv = KFold(k=5)

    # basic cross validation loop.
    # I've zipped together a range and the splits into order to get fold no.
    for i, split_data in zip(range(cv.get_n_splits(X)), cv.split(X, y)):
        train_X, train_y, test_X, test_y = split_data
        print(f'Fold {i+1}:\nTrain:\tX:{train_X}, y:{train_y}')
        print(f'Test:\tX:{test_X}, y:{test_y}')
        


