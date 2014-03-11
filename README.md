FeatureMatrix
=============

This is a helper class for turning key-value lists into a matrix of float or binary features.  It stores the matrix internally in sparse representation, and may be converted to a dense matrix for training or testing models (especially scikit-learn)

    fmat = featureMatrix.FeatureMatrix(rowNameLst = [], colNameLst = [], noNewCols = False, noNewRows = False, matrix = [], dtype = np.float64)

Parameters
----------

rowNameLst: Ordered list of row labels
colNameLst: Ordered list of column labels
noNewRows: If set to True, prevents new rows from eing added to matrix
noNewCols: If set to True, prevents new columns from being added to matrix
matrix: [[rowName, colName, value]] sparse representation of the feature matix
dtype: datatype for storing matrix values

Attributes
----------