"""Charges: output a file containing matrix index pairs.
"""

# Author: Dave Press
#import codecs
import numpy as np

class FloatFeatureMat(object):	
	def __init__(self, rowNameIdx = [], colNameIdx = [], matrix = [], noNewCols = False, noNewRows = False):
		""""""
		self.rowNameIdx = rowNameIdx
		self.colNameIdx = colNameIdx
		self.numRows = len(rowNameIdx)
		self.numCols = len(colNameIdx)		
		self.rowNameMap = {}
		self.colNameMap = {}
		for r in range(self.numRows):
			self.rowNameMap[self.rowNameIdx[r]] = r
		for c in range(self.numCols):
			self.colNameMap[self.colNameIdx[c]] = c
		self.matrix = matrix
		self.noNewCols = noNewCols
		self.noNewRows = noNewRows
			
	def add(self, rowName, colName, val=1.0):
		""""""
		if (self.rowNameMap.get(rowName) != None or not self.noNewRows) and (self.colNameMap.get(colName) != None or not self.noNewCols):
			if self.rowNameMap.get(rowName) == None:
				self.rowNameIdx.append(rowName)
				self.rowNameMap[rowName] = self.numRows
				self.numRows += 1
			if self.colNameMap.get(colName) == None:
				self.colNameIdx.append(colName)
				self.colNameMap[colName] = self.numCols
				self.numCols += 1
			matrixTriple = [self.rowNameMap[rowName], self.colNameMap[colName], np.float32(val)]
			self.matrix.append(matrixTriple)
						 

	def addFile(self, fileName, skip_lines = 1, rowNameInd = 0, colNameInd = 1,
				 valInd = 2, delimiter = '|', binaryFeatures = []):
		""""""
		file = open(fileName, 'r')
		for l in range(skip_lines):
			hdr = file.readline()
		while True:
			line = file.readline()
			if line == '':
				break
			tokens = line.split('\n')[0].split(delimiter)
			if binaryFeatures == []:
				if len(tokens)==3:
					binaryFeatures = False
				else:
					binaryFeatures = True
			if binaryFeatures:	
				self.add(tokens[rowNameInd], tokens[colNameInd], 1.0)
			else:
				self.add(tokens[rowNameInd], tokens[colNameInd], tokens[valInd])
		file.close()
		
	def toDenseMatrix(self):
		"""Parse the sql table"""
		denseMat = np.zeros((self.numRows,self.numCols),dtype=np.float32)
		for rc in self.matrix:
			denseMat[rc[0],rc[1]] = rc[2]
		return denseMat
		

	


