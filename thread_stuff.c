#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

pthread_mutex_t lock;

void *run(void *arg) {

	/*
	pthread_mutex_lock(&lock);
	printf("In thread\n");
	pthread_mutex_unlock(&lock);
	*/

	// busy work
	for (int i = 0; i < 100000000; i++);

	free(arg);
	return NULL;
}

int main(int argc, char *argv[]) {

	if (argc != 2) {
		return 1;
	}

	int NUM_THREADS = atoi(argv[1]);

	pthread_t tid;

	for (int i = 0; i < NUM_THREADS; i++) {
		pthread_create(&tid, NULL, run, NULL);
	}

	pthread_exit(NULL);
	return 0;
}
