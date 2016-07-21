To create graph file:
   1) Create normalized scores from a phyloP p-scores file (ENSGT00390000007772.outP).
   
      python normalized.py ENSGT00390000007772.outP normalized.txt

      Ensure the header of the outP file has been removed!
      Normalized.py can be found in ../MakeGraph/

   2) Your alignment file should have one extra specie as explained in the .tex file,
      example can be found here (ENSGT00390000007772.fa)

   3) Make sure the name of the files and size of alignment are correct in the .tex file.

   4) Now the .tex file may be used to create the graph. Sample output can be found here.
      (ENSGT00390000007772.pdf)