#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * infinite_while - Function.
 *
 * Description: Runs an infinite loop.
 *
 * Return: 0 (Always).
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - Entry point.
 *
 * Description: Creates 5 running zombie process.
 *
 * Return: 0 (Always).
 */
int main(void)
{
	pid_t pid;
	int i = 0;

	while (i < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			i++;
		}
		else
			exit(0);
	}
	infinite_while();

	return (0);
}
