#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int add(int a[], int num) {
	int result = 2;
	for (int i = 0; i < num; i++) {
		result = result + a[i];
	}
	return result;
}

int main(void) {

	int testcase;
	int n_sample;
	int answer[100];

	char input[100];
	int input_int[100];

	//printf("Number of testcase: ");
	scanf("%d", &testcase);

	for (int i = 0; i < testcase; i++) {
		//printf("\n************************************");
		//printf("\nNumber of samples for testcase.%d: ",i);
		scanf("%d", &n_sample);
		//printf("input string : ");
		scanf(" %[^\n]", input);
		char *ptr = strtok(input, " ");

		int j = 0;
		while (ptr != NULL)
		{
			input_int[j++] = atoi(ptr);
			ptr = strtok(NULL, " ");
		}
		answer[i] = add(input_int, n_sample);
	}

	for (int i = 0; i < testcase; i++) {
		printf("\n%d", answer[i]);
		//printf("\nresult for case%d : %d", i, answer[i]);
	}

	return 0;
}

