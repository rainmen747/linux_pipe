#include <fcntl.h>

#include <sys/stat.h>

#include <unistd.h>

#include <stdio.h>

#include <stdlib.h>


#define MSG_SIZE 80


int main()

{

    char msg[MSG_SIZE];

    int filedes;

    int nread, cnt;

      if(access("/tmp/rain_pipe",F_OK) == -1)
    {
  

    if (mkfifo("/tmp/rain_pipe",0666) == -1){

        printf("fail to call fifo()\n");

        exit(1);

    }

}

    if((filedes = open("/tmp/rain_pipe",O_RDWR)) < 0){

        printf("fail to call fifo()\n");

        exit(1);

    }


    while(1){

        if((nread = read(filedes, msg, MSG_SIZE)) < 0 ){

            printf("fail to call read()\n");

            exit(1);

        }

        printf("%s", msg);

    }

    unlink("/tmp/rain_pipe");


    return 0;

}
