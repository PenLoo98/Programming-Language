#include <stdio.h>
#include <stdlib.h>

#define INITIAL_CAPACITY 4

typedef struct {
    int *items;
    int capacity;
    int length;
} List;

List *create_list() {
    List *list = malloc(sizeof(List));
    list->items = malloc(sizeof(int) * INITIAL_CAPACITY);
    list->capacity = INITIAL_CAPACITY;
    list->length = 0;
    return list;
}

void resize_list(List *list, int new_capacity) {
    int *new_items = realloc(list->items, sizeof(int) * new_capacity);
    if (new_items != NULL) {
        list->items = new_items;
        list->capacity = new_capacity;
    }
}

void append(List *list, int item) {
    if (list->length >= list->capacity) {
        resize_list(list, list->capacity * 2);
    }
    list->items[list->length++] = item;
}

void insert(List *list, int index, int item) {
    if (index < 0 || index > list->length) {
        return;  // do nothing if index is out of bounds
    }
    if (list->length >= list->capacity) {
        resize_list(list, list->capacity * 2);
    }
    for (int i = list->length; i > index; i--) {
        list->items[i] = list->items[i - 1];
    }
    list->items[index] = item;
    list->length++;
}

int pop(List *list, int index) {
    if (index < 0 || index >= list->length) {
        return -1;  // return -1 if index is out of bounds
    }
    int item = list->items[index];
    for (int i = index; i < list->length - 1; i++) {
        list->items[i] = list->items[i + 1];
    }
    list->length--;
    if (list->length <= list->capacity / 4) {
        resize_list(list, list->capacity / 2);
    }
    return item;
}

void print_list(List *list) {
    printf("[");
    for (int i = 0; i < list->length; i++) {
        printf("%d", list->items[i]);
        if (i < list->length - 1) {
            printf(", ");
        }
    }
    printf("]\n");
}

void free_list(List *list) {
    free(list->items);
    free(list);
}

int main() {
    List *my_list = create_list();
    append(my_list, 3);
    append(my_list, 7);
    append(my_list, 1);
    print_list(my_list);
    insert(my_list, 1, 5);
    print_list(my_list);
    int popped_item = pop(my_list, 2);
    printf("popped item: %d\n", popped_item);
    print_list(my_list);
    free_list(my_list);
    return 0;
}
