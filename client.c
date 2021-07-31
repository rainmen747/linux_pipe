#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MSG_SIZE 1000

int main()
{
    char msg[MSG_SIZE];
    int filedes;
    int cnt;

    // open fifo file

    if((filedes = open("/tmp/rain_pipe", O_WRONLY)) < 0){

        printf("fail to call open()\n");

        exit(1);

    }
  
  

  for(cnt=0; cnt<10; cnt++){

       // sprintf(msg,"%s %d\n","good test",cnt);
        for (int ix=0;ix<1000;ix++) msg[ix]=cnt % 255;
        if(write(filedes, msg, 1023)==-1){

            printf("fail to call write()\n");

            exit(1);

        }


	}
  
/*

    for(cnt=0; cnt<3; cnt++){

        printf("input a message : ");

        scanf("%s",msg);

        msg[MSG_SIZE-1] = '\0';


        if(write(filedes, msg, MSG_SIZE)==-1){

            printf("fail to call write()\n");

            exit(1);

        }

        sleep(1);

    }
*/
}
