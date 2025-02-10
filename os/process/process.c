#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

#ifdef _WIN32
#include <windows.h>
#define getppid() (0)  // Windows does not have getppid, so we define it as 0
#endif


int main() {
    pid_t process_id = getpid();   // Current process ID
    pid_t parent_process_id = getppid();  // Parent process ID

    printf("Current Process ID: %d\n", process_id);
    printf("Parent Process ID: %d\n", parent_process_id);

    return 0;
}