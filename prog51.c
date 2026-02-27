#include <stdio.h>
#include <stdlib.h>

// Structure for linked list node
struct Node {
    int data;
    struct Node* next;
};

// Create new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Insert at end
struct Node* insertEnd(struct Node* head, int data) {
    struct Node* newNode = createNode(data);

    if (head == NULL)
        return newNode;

    struct Node* temp = head;
    while (temp->next != NULL)
        temp = temp->next;

    temp->next = newNode;
    return head;
}

// Find length of list
int getLength(struct Node* head) {
    int count = 0;
    while (head != NULL) {
        count++;
        head = head->next;
    }
    return count;
}

// Find intersection point
void findIntersection(struct Node* head1, struct Node* head2) {
    int len1 = getLength(head1);
    int len2 = getLength(head2);

    int diff;
    struct Node* ptr1 = head1;
    struct Node* ptr2 = head2;

    // Move pointer of longer list
    if (len1 > len2) {
        diff = len1 - len2;
        for (int i = 0; i < diff; i++)
            ptr1 = ptr1->next;
    } else {
        diff = len2 - len1;
        for (int i = 0; i < diff; i++)
            ptr2 = ptr2->next;
    }

    // Traverse together
    while (ptr1 != NULL && ptr2 != NULL) {
        if (ptr1->data == ptr2->data) {
            printf("%d\n", ptr1->data);
            return;
        }
        ptr1 = ptr1->next;
        ptr2 = ptr2->next;
    }

    printf("No Intersection\n");
}

int main() {
    int n, m, val;
    struct Node* head1 = NULL;
    struct Node* head2 = NULL;

    // First list
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &val);
        head1 = insertEnd(head1, val);
    }

    // Second list
    scanf("%d", &m);
    for (int i = 0; i < m; i++) {
        scanf("%d", &val);
        head2 = insertEnd(head2, val);
    }

    findIntersection(head1, head2);

    return 0;
}