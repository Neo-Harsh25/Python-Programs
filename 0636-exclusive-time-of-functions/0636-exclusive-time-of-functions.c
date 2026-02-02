/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

typedef struct ll {
    struct ll *next;
    int id;
    int time;
} ll;

void insertStack(ll **stack, int id, int time){
    // push to top of stack
    ll *node = malloc(sizeof(ll));
    node->id = id;
    node->time = time;
    node->next = *stack;
    *stack = node;
    return;
}

int popStack(ll **stack, int id, int time){
    // pop from stack
    ll *tmp = *stack;
    int retval = 0;

    *stack = (*stack)->next;
    retval = time - tmp->time + 1;
    free(tmp);

    tmp = *stack;

    // move all remaining values in the stack forward by elapsed time
    while(tmp){
        tmp->time += retval;
        tmp = tmp->next;
    }

    return retval;
}



int* exclusiveTime(int n, char** logs, int logsSize, int* returnSize) {
    int *timings = calloc(n, sizeof(int));
    ll *stack = NULL;
    char *log, *endptr, signal;
    int id, time, elapsed = 0;

    for(int i=0; i<logsSize; i++){
        id = strtol(logs[i], &endptr, 10);
        endptr++;
        signal = *endptr;
        endptr += signal == 's' ? 6 : 4;
        time = strtol(endptr, NULL, 10);
        if(signal == 's'){
            insertStack(&stack, id, time);
        } else {
            time = popStack(&stack, id, time);
            timings[id] += time;
        }
    }

    *returnSize = n;
    return timings;
}