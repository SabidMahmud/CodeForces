// count the maximum number of domino to cover a rectangular board
#include <stdio.h>

#define domino_area (2 * 1)
int main(void) {
  int M, N; // Shape of a rectangular board of MxN;
  float area, domino_count;
  scanf("%d %d", &M, &N);
  if (1 <= M && M <= N && N <= 16) {
    area = M * N;
    domino_count = area / domino_area;
    printf("%d\n", (int)domino_count);
  }
  return 0;
}