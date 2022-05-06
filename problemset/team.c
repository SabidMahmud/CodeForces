// A program to calculate how many problem they can solve
#include <stdio.h>
#include <stdlib.h>
int main(void) {
  int n; // Number of the test cases (problems)
  int frnd1, frnd2, frnd3, problems = 0;
  scanf("%d", &n); // Read the number of the test cases
                   // Start a loop to take input n times
  for (int i = 1; i <= n; i++) {
    scanf("%d %d %d", &frnd1, &frnd2, &frnd3);
    
    // check how many of them can solve a problem;
    if (
        (frnd1 == 1 && frnd2 == 1) ||
        (frnd2 == 1 && frnd3 == 1) ||
        (frnd3 == 1 && frnd1 == 1)
       ) {
           problems += 1; // Calculate how many problems they can solve
    }
  }
  printf("%d\n", problems);
  return 0;
}