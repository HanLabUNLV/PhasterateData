This folder contains data from the paper used to fit F84 and F84e models, as well as
fitted models, computed likelihoods, and p-values.

Folders:

AlignmentFiles/
	Genetree alignment files for primate trees with human and five or more species.
	These file come from ensembl but have been gblocked to clean up messy areas and
	filtered to only include files with no indel event of length 30 or more. Files
	are in fasta format.

NewickFiles/
	Newick tree files corresponding to phylogenetic trees for the AlignmentFiles.

F84PrimeModelResults/
	Fitted models, p-scores, likelihoods, and p-values for data fitted through
	PhyloFit using the above fasta files and newick trees. Likelihoods and p-scores
	created by using PhyloP on our fitted models files. P-values created by running
	the scripts in the top level Scripts/ folder.

	This data is for the F84e modified model. That is, the F84 model extended with
	gaps and then modified to allow multiple indel events per site as described on
	the paper.

F84ModelResults/
	Fitted models, p-scores, likelihoods, and p-values for data fitted through
	PhyloFit using the above fasta files and newick trees. Likelihoods and p-scores
	created by using PhyloP on our fitted models files. P-values created by running
	the scripts in the top level Scripts/ folder.

	This data is for the F84 model as described by Felsentein and Churchill 1996.

F84RivasModelResults/
	Fitted model using the above fasta files and newick trees.

	This data is for the F84e model as described by Rivas and Eddy 2008.

allBranchLengths.txt
        List of all branch lengths for our 30 gaps or less data. This was used to compute
        the average branch length of our entire data.
