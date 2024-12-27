#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {

	printf("before fork\n");

	int pid;

	for (int i = 0; i < 12; i++) {
		pid = fork();
		if (pid < 0) {
			perror("Fork failed\n");
			return 1;
		} else if (pid == 0) {
			printf("Child: %d\n", getpid());
			_exit(0);
		} else {
			wait(NULL);
		}
	}

	printf("Parent process: %d\n", getpid());
	return 0;
}
