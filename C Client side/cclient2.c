#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <mysql/mysql.h>
#define MAX 80
#define PORT 8080
#define SA struct sockaddr
   
int main()
{
    MYSQL *conn;
    MYSQL_RES *res;
    MYSQL_ROW row;
    char *server = "172.18.0.2";
    char *user = "root";
    char *password = "123";
    char *database = "users";


    int sockfd, connfd;
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
    servaddr.sin_addr.s_addr = inet_addr("172.18.0.5");
    servaddr.sin_port = htons(PORT);
   
    // connect the client socket to server socket
    if (connect(sockfd, (SA*)&servaddr, sizeof(servaddr)) != 0) {
        printf("connection with the server failed...\n");
        exit(0);
    }
    else
        printf("connected to the server..\n");
  
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
        
        printf("User \t\t Points  time\n");
        printf("=========================================\n");
            while ((row = mysql_fetch_row(res))) {
                printf("%s\t %s\t %s\t\n", row[0], row[1], row[2]);
            }
            printf("=========================================\n");
        /* Release memory used to store results and close connection */
        mysql_free_result(res);
        mysql_close(conn);
        sleep(4);
    }

    // close the socket
    close(sockfd);
}