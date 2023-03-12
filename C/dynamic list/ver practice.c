#include <stdio.h>
#include <stdlib.h>

#define STACK_SIZE 10

int top = -1;               // top 초기화
int size = 1;

int isEmpty() {
	if (top == -1) return 1;
	else return 0;
}

int isFull() {
	if (top % STACK_SIZE == 9) return 1;
	else return 0;
}

// 스택의 top에 원소를 삽입하는 연산 == append()
void append(int item) {
	int *temp;

	if (isFull()) {
		printf(" Full STACK\n");
		temp = (int*)malloc((STACK_SIZE * size)* sizeof(int));

		for (int i = 0; i < (top + 1); i++) temp[i] = stack[i];
		stack = (int*)malloc((STACK_SIZE * (size + 1))* sizeof(int));

		for (int i = 0; i < (top + 1); i++) stack[i] = temp[i];
		stack[++top] = item;  // top을 증가시킨 후 현재 top에 원소 삽입

		size++;

		free(temp);

	}
	else stack[++top] = item;  // top을 증가시킨 후 현재 top에 원소 삽입
}

// 스택의 index에 원소를 삽입하는 연산 == insert()
void insert(int index, int item) {
	int *temp;

	if (isFull()) {
		printf(" Full STACK\n");
		temp = (int*)malloc((STACK_SIZE * size)* sizeof(int));

		for (int i = 0; i < (top + 1); i++) temp[i] = stack[i];
		stack = (int*)malloc((STACK_SIZE * (size + 1))* sizeof(int));

		for (int i = 0; i < (top + 1); i++) stack[i] = temp[i];
		stack[++top] = item;  // top을 증가시킨 후 현재 top에 원소 삽입

		size++;

		free(temp);

	}
	else {
		for (int i = top; i > index; i--) stack[i] = stack[i - 1];
		stack[index] = item;  // top을 증가시킨 후 현재 top에 원소 삽입
		top++;
	}
}

// 스택의 top에 있는 원소를 삭제하는 연산 == pop()
int pop() {
	if (isEmpty()) {
		printf(" Empty STACK\n");
		return -1;
	}
	else return stack[top--];  // top을 감소시킨 후 현재 top에 있는 원소 반환
}

// 스택의 원소를 출력하는 연산
void printStack() {
	int i;
	printf(" STACK SIZE [%d]\n", (STACK_SIZE * size));
	printf("\n STACK [ ");
	for (i = 0; i <= top; i++) printf("%d ", stack[i]);
	printf("]\n");
}

int main(void) {
    stack = (int*)malloc(STACK_SIZE * sizeof(int));
    
    int i;
    for (i = 0; i < 44; i++) append(i + 1);
    printStack();	
    for (i = 0; i < 7; i++) printf(" POP Data [%d]\n", pop());
    printStack();

    free(stack);
    getchar();
}