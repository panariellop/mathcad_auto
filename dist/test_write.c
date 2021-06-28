#include <stdio.h>
#include <string.h>

int main(void){
FILE *fpt;
fpt = fopen("MyFile.csv", "w+");
int id = 12; char name[] = "Piero1"; char email[] = "piero@gmaiaasdfl.com"; char phone[] = "12d1234132";
fprintf(fpt,"ID, Name, Email, Phone Number\n");
fprintf(fpt,"%d, %s, %s, %s\n", id, name, email, phone);
fclose(fpt);
return 0;
}


