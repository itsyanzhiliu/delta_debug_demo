# Demo of Delta Debugging

implement delta debugging (DD) to reduce to an input but still preserves its interestingness as specified by an oracle (e.g., it crashes, or does something interesting). 

DD program can take as input a C program (e.g., `myfile.c`) and an oracle in a form of a test script that defines interestingness (e.g., a `test.sh` that takes as input a `C` file, 
compiles and runs it, and returns **0** if it is interesting and **1** if it is not). The program applys DD to obtain a minimal version of `myfile.c` that is still interesting.
