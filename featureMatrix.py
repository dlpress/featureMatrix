import numpy as np

# Author: David Press
# Created: 2014_03_10

class FeatureMat(object):
	def __init__(self, rowNameLst = [], colNameLst = [], noNewCols = False, noNewRows = False, matrix = [], dtype = np.float64):
		self.nRows = len(rowNameLst)
		self.nCols = len(colNameLst)	
		self.rowNameLst = rowNameLst
		self.colNameLst = colNameLst

		self.rowNameMap = {}
		self.colNameMap = {}
		for r in range(self.nRows):
			self.rowNameMap[self.rowNameLst[r]] = r
		for c in range(self.nCols):
			self.colNameMap[self.colNameLst[c]] = c
		self.matrix = matrix
		self.noNewCols = noNewCols
		self.noNewRows = noNewRows
		self.dtype = dtype
			
	def add(self, rowName, colName, value=1.0):
		""""""
		if ((rowName in self.rowNameMap) or not self.noNewRows) and ((colName in self.colNameMap) or not self.noNewCols):
			if rowName not in self.rowNameMap:
				self.rowNameLst.add(rowName)
				self.rowNameMap[rowName] = self.nRows
				self.nRows += 1
			if colName not in self.colNameMap:
				self.colNameLst.add(colName)
				self.colNameMap[colName] = self.nCols
				self.nCols += 1
			triplet = [self.rowNameMap[rowName], self.colNameMap[colName], value]
			self.matrix.add(triplet)
						 
	def addFile(self, file_name, skip_lines = 1, rowNameInd = 0, colNameInd = 1, valueInd = 2, delim = '|', binaryFeatures = []):
		""""""
		f = open(file_name, 'r')
		for line in range(skip_lines):
			header = f.readline()
		while True:
			line = f.readline()
			if line == '':
				break
			tokens = line.split('\n')[0].split(delim)
			if binaryFeatures == []:
				if len(tokens)==3:
					binaryFeatures = False
				else:
					binaryFeatures = True
			if binaryFeatures:	
				try:
					self.add(tokens[rowNameInd], tokens[colNameInd], 1)
				except:
					print tokens
			else:
				self.add(tokens[rowNameInd], tokens[colNameInd], np.array(tokens[valueInd],self.dtype))
		f.close()
		
	def toDenseMatrix(self, dtype=None):
		if dtype==None:
			dtype=self.dtype
		denseMatrix = np.zeros((self.nRows, self.nCols), dtype=dtype)
		for triplet in self.matrix:
			denseMatrix[triplet[0],triplet[1]] = triplet[2]
		return denseMatrix
		

	


