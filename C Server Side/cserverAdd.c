#include <stdio.h>
#include <netdb.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <mysql/mysql.h>
#include <time.h>
#define MAX 80
#define PORT 8080
#define SA struct sockaddr

const char * get_month(int n)
{
    switch(n)
    {
        case 1:
            return " Jan";
        case 2:
            return " Feb";
        case 3:
            return " March";
        case 4:
            return " April";
        case 5:
            return " May";
        case 6:
            return " June";
        case 7:
            return " July";
        case 8:
            return " August";
        case 9:
            return " September";
        case 10:
            return " October";
        case 11:
            return " November";
        case 12:
            return " December";
    }
}


int main() {
	MYSQL *conn;
	MYSQL_RES *res;
	MYSQL_ROW row;
	char *server = "172.18.0.2";
	char *user = "root";
	char *password = "123";
	char *database = "users";
      
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
	
	char *uname, st[10];
	int point;
	
	//get date from maschine server
	
	time_t t = time(NULL);
	struct tm tm = *localtime(&t);
    
	const char * month = get_month(tm.tm_mon + 1);
	int day = tm.tm_mday;
	sprintf(st, "%d", day);
	strcat(st, month);
	//sprintf(smonth, " %d", month);

	//printf("%s %d %d \n",sday, day, month);
	
	printf("Please enter username : ");
	scanf(" %[^\n]*s", uname);
	

	printf("Please enter points : ");
	scanf(" %d", &point);
	
	
	char sql[100];  
	sprintf(sql, "INSERT INTO user(user,points,datetime_stamp,origin_server) VALUES ('%s', %d, '%s', 'C Server')", uname, point, st);
	if (mysql_query(conn, sql)) {
		fprintf(stderr, "%s\n", mysql_error(conn));
	}
	else {	
		printf("Successfully added user to database\n");
	}
		
	//printf("User \t\t Points \t time\n");
	//printf("=========================================\n");
	while ((row = mysql_fetch_row(res))) {
		//printf("%s\t\t %s\t\t %s\n", row[0], row[1], row[2]);
	}
	//printf("=========================================\n\n\n");
	
	/* Release memory used to store results and close connection */
	mysql_free_result(res);
	mysql_close(conn);
}