#include <stdio.h>

int main()
{
	int y=0;
	while(1){
		y+=10;
		for (int ix=0;ix<1000;ix++) printf("%d ",(ix+y) % 200);
		printf("\n");
		
	}
	return 1;

}
