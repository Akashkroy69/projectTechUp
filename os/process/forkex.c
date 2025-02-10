#include <stdio.h>
#include <unistd.h>

int main() {
    int pid = fork();  // Create a child process. this is a system call for UNIX/Linux to create a process
    // int pid = CreateProcess(); this is a system call for windows system to create a process

    if (pid == 0) {
        // Child process
        printf("This is the child process with PID: %d\n", getpid());
    } else {
        // Parent process
        printf("This is the parent process with PID: %d\n", getpid());
    }

    return 0;
}
