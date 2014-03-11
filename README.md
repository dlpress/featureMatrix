FeatureMatrix
=============

This is a helper class for turning key-value lists into a matrix of float or binary features.  It stores the matrix internally in sparse representation, and may be converted to a dense matrix for training or testing models (especially scikit-learn).  

    fmat = featureMatrix.FeatureMatrix(rowNameLst = [], colNameLst = [], 
		noNewCols = False, noNewRows = False, matrix = [], dtype = np.float64)

Parameters
----------

* rowNameLst: Ordered list of row labels
* colNameLst: Ordered list of column labels
* noNewRows: If set to True, prevents new rows from eing added to matrix
* noNewCols: If set to True, prevents new columns from being added to matrix
* matrix: [[rowName, colName, value]] sparse representation of the feature matix
* dtype: datatype for storing sparse matrix values internally

Attributes
----------

* rowNameMap: a dictionary containing indexes of row labels
* colNameMap: a dictionary containing indexes of column labels
* nRows: Number of rows in the matrix
* nCols: Number of columns in the matrix

Methods
-------

* **add**(rowName, colName[, value=1.0]):

Adds a single element to the matrix.  If the same row-column combination contain multiple entries, only the most recent value is used.

* **addFile**(file_name[, skip_lines=1, rowNameInd = 0, colNameInd = 1, valueInd = 2, delim = '|', binaryFeatures = []]):

Adds all features stored in a flatfile to the feature matrix.  Typical flatfile format may be:
| RowName  | ColumnName | Value |
| ------------- | ------------- | ----------- |
| label1 | feat1  | 1.1 |
| label2  | feat1  | 2.2 |

* **toDenseMatrix**([dtype = None]):

Returns a dense numpy matrix representation of the features. Data type is same as feature matrix, unless specified otherwise in parameter.

