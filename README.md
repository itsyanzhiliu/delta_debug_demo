# Demo of Delta Debugging

implement delta debugging (DD) to reduce to an input but still preserves its interestingness as specified by an oracle (e.g., it crashes, or does something interesting). 

DD program can take as input a C program (e.g., `myfile.c`) and an oracle in a form of a test script that defines interestingness (e.g., a `test.sh` that takes as input a `C` file, 
compiles and runs it, and returns **0** if it is interesting and **1** if it is not). The program applys DD to obtain a minimal version of `myfile.c` that is still interesting.

## Running DD
```terminal
$ > python dd.py  hello1.c -test hello1.test
preprocessing .. rm 1 idxs: [16]
can delete 2 chunks containing 2 idxs: [0, 1]
can delete 1 chunks containing 1 idxs: [2]
can delete 1 chunks containing 1 idxs: [5]
can delete 2 chunks containing 2 idxs: [6, 7]
can delete 2 chunks containing 2 idxs: [10, 11]
can delete 1 chunks containing 1 idxs: [15]
can delete 6 chunks containing 9 idxs: [0, 1, 2, 5, 6, 7, 10, 11, 15]
can delete 1 chunks containing 9 idxs: [0, 1, 2, 5, 6, 7, 10, 11, 15]
done: '/Users/tnguyen/git/projects/vdd/src/min.c' (lines: total 8 rem 9, 29 created variants)
```

```c
// min.c: reduced program
int main(int argc, char **argv) {
    int a = 0;
    a+=2;
    a++;
    if (a >= 3){
      printf("correct\n");
    }
}
```
