#Suzumo has a chessboard with N rows and M columns.
#In one step, he can choose two cells of the chessboard which share a common edge 
#(that has not been cut yet) and cut this edge.

#Formally, the chessboard is split into two or more pieces if it is
#possible to partition its cells into two non-empty subsets S1 and S2
#such that S1∩S2=∅ (phi)
# |S1|+|S2|=NM
#such that there is no pair of cells c1,c2
#c1∈S1,c2∈S2
#which share a common edge that has not been cut.
Suzumo does not want the board to split into two or more pieces.
#Compute the maximum number of steps he can perform while satisfying this condition.

