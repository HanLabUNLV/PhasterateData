This folder contains helpful scripts for calculating p-values on a per file basis for the
output of phyloP.

PhyloP will output a computedLikelihoods.txt file, this contains three rows of data:
-18.020846	-10.393778	38.851633
-18.199452	-10.600930	38.036582
-17.973770	-10.339081	39.080146
-17.978035	-10.346858	38.967353
-18.199452	-10.600930	38.036582
-17.973770	-10.339081	39.080146
-18.020846	-10.393778	38.851633
-17.978035	-10.346858	38.967353
-18.199452	-10.600930	38.036582

Where the first column is the log-likelihood scores for the null-model, the second column
for the alt-model and the last column the scaling factors.

makePValues.sh:
	Given the computedLikelihoods.txt file, it will output a pValues.txt, with one
	degree of freedom using a chi-square distribution.

The scripts are more general:

lrtTest.py:
	Given two files containing the log likelihood scores. It will perform a likelihood
	ratio test. The files must contain a single column of floats separated by
	newlines.


pValues.py:
	Given a file it will compute the p-values based on the passed degrees of freedom
	using a chi-squared distribution.