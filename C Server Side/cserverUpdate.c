#include <stdio.h>
#include <stdio.h>
#include <netdb.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <mysql/mysql.h>
#define MAX 80
#define PORT 8080
#define SA struct sockaddr

int main() {
	MYSQL *conn;
	MYSQL_RES *res;
	MYSQL_ROW row;
	char *server = "172.18.0.2";
	char *user = "root";
	char *password = "123";
	char *database = "users";
   
   
	int sockfd, connfd, len;
    struct sockaddr_in servaddr, cli;
   
    // socket create and verification
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1) {
        printf("socket creation failed...\n");
        exit(0);
    }
    else
        printf("Socket successfully created..\n");
    bzero(&servaddr, sizeof(servaddr));
   
    // assign IP, PORT
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(PORT);
   
    // Binding newly created socket to given IP and verification
    if ((bind(sockfd, (SA*)&servaddr, sizeof(servaddr))) != 0) {
        printf("socket bind failed...\n");
        exit(0);
    }
    else
        printf("Socket successfully binded..\n");
   
    // Now server is ready to listen and verification
    if ((listen(sockfd, 5)) != 0) {
        printf("Listen failed...\n");
        exit(0);
    }
    else
        printf("Server listening..\n");
    len = sizeof(cli);
   
    // Accept the data packet from client and verification
    connfd = accept(sockfd, (SA*)&cli, &len);
    if (connfd < 0) {
        printf("server accept failed...\n");
        exit(0);
    }
    else
        printf("server accept the client...\n");
   
    // After chatting close the socket
    close(sockfd);
   
   
   /*===============================*/
   
   
	while(1){

		conn = mysql_init(NULL);

		/* Connect to database */
		if (!mysql_real_connect(conn, server,
			 user, password, database, 0, NULL, 0)) {
		  fprintf(stderr, "%s\n", mysql_error(conn));
		  return(0);
		}
		/* send SQL query */
		if (mysql_query(conn, "SELECT * from user WHERE origin_server='C Server'")) {
		  fprintf(stderr, "%s\n", mysql_error(conn));
		  return(0);
		}
		res = mysql_store_result(conn);


		int point;
		int pointUpd;
		char *name;
		printf("User \t\t Points  time\n");
		printf("=========================================\n");
			while ((row = mysql_fetch_row(res))) {
				point = atoi(row[1]);
				name = row[0]; 
				printf("%s\t %s\t %s\t\n", row[0], row[1], row[2]);
				pointUpd = point + 10;
				char sql[100];  
				sprintf(sql, "UPDATE user SET points = %d WHERE user = '%s' AND origin_server='C Server'", pointUpd, name);
				if (mysql_query(conn, sql)) {
					fprintf(stderr, "%s\n", mysql_error(conn));
				}
			}
			printf("=========================================\n");
		
		
		/* Release memory used to store results and close connection */
		mysql_free_result(res);
		mysql_close(conn);
		sleep(4);
	}
}