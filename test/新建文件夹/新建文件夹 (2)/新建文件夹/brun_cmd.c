#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h> 
#include <unistd.h> 

int main(int argc, char** argv)
{
	//printf(" UID\t= %d\n", getuid());
    //printf(" EUID\t= %d\n", geteuid());
    //printf(" GID\t= %d\n", getgid());
    //printf(" EGID\t= %d\n", getegid());

	uid_t uid ,euid; 
	uid = getuid() ; 
	euid = geteuid(); 
	//printf("my uid :%u\n",getuid()); //这里显示的是当前的uid 可以注释掉. 
	//printf("my euid :%u\n",geteuid()); //这里显示的是当前的euid 
	//if(setreuid(euid, uid)) //交换这两个id 
	if(setreuid(0, 0)) //交换这两个id 
		perror("setreuid"); 
	//printf("after setreuid uid :%u\n",getuid()); 
	//printf("afer sertreuid euid :%u\n",geteuid());
	if(setregid(0, 0))
		perror("setregid");

	//printf(" UID\t= %d\n", getuid());
    //printf(" EUID\t= %d\n", geteuid());
    //printf(" GID\t= %d\n", getgid());
    //printf(" EGID\t= %d\n", getegid());

	char a[256];
	if (argc==2)
		sprintf(a, "export LANG=zh_CN.UTF-8;bash run_cmd.sh %s", argv[1]);
	else
		sprintf(a, "export LANG=zh_CN.UTF-8;bash run_cmd.sh");
	system(a);
	return 0;
}
