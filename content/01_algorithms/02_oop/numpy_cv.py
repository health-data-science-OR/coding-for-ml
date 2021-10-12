'''
temp store for numpy classes
'''

class LeaveNOut:
    '''
    Leave n samples out cross validation of a X, y formatted dataset.
    When n = 1 this is equivalent to Leave 1 out cross validation (LOOCV)
    Note that when `n` is greater than 1 the train, test folds are overlapping.
    Warning: Computationally expensive for large datasets.

    '''
    def __init__(self, n=1):
        '''
        Params:
        -------
        n: int
            The number of data points to leave out of each 
        '''
        self.n = n
    
    def __repr__(self):
        return f'LeaveNOut(n={self.n}'

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
        
        #create the folds
        for test_index in range(0, len(X), self.n):
        
            # training data indexes
            train_X = np.concatenate([X[:test_index], X[test_index + self.n:]])
            train_y = np.concatenate([y[:test_index + self.n], y[test_index + self.n:]])
            
            # test data
            test_X, test_y = X[test_index: test_index+self.n], y[test_index: test_index+self.n]
            
            yield train_X, test_X, train_y, test_y
            
            
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