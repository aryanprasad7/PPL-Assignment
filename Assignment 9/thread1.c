#include<stdio.h>
#include<pthread.h>
#include<unistd.h>

void *justfunction(void *arg);

/* Infinite loop printing Atharva here : 111803142 */

int main() {

	pthread_t thread_id;
	pthread_create(&thread_id, NULL, justfunction, NULL);
	pthread_join(thread_id, NULL);
	
	return 0;
}


void *justfunction(void *arg) {
	
	while(1) {
		printf("Atharva here : 111803142\n");
		sleep(1);
	}
	
	return NULL;
}