#include <stdio.h>

int main()
{
	for(int i=0;i<100;i++){
		for (int ix=0;ix<1000;ix++) printf("%d,",ix);
		printf("\n");
	}
	return 1;

}
