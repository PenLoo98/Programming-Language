#include <stdio.h>
#include <stdlib.h>

#define STACK_SIZE 10

int *stack;
int top = -1;
int size = 1;

int isEmpty() {
    if (top == -1) return 1;
    else return 0;
}

int isFull() {
    if (top == STACK_SIZE - 1) return 1;
    else return 0;
}

void append(int item) {
    if (isFull()) {
        printf("Stack is full\n");
        return;
    }
    stack[++top] = item;
}

void insert(int index, int item) {
    if (isFull()) {
        printf("Stack is full\n");
        return;
    }
    if (index > top) {
        printf("Invalid index\n");
        return;
    }
    for (int i = top + 1; i > index; i--) {
        stack[i] = stack[i - 1];
    }
    stack[index] = item;
    top++;
}

int pop() {
    if (isEmpty()) {
        printf("Stack is empty\n");
        return -1;
    }
    return stack[top--];
}

void printStack() {
    printf("Stack size: %d\n", top + 1);
    printf("Stack [ ");
    for (int i = 0; i <= top; i++) {
        printf("%d ", stack[i]);
    }
    printf("]\n");
}

int main(void) {
    stack = (int*)malloc(STACK_SIZE * sizeof(int));
    int i = 0;
    while (!isFull()) {
        append(++i);
    }
    append(99); // should fail
    printStack();
    for (i = 0; i < 7; i++) {
        printf("POP data [%d]\n", pop());
    }
    printStack();
    free(stack);
    return 0;
}
