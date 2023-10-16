/*Hotel_Management_System*/

#include <stdio.h>
#include <string.h>
//__Global Arrays__//
int rooms_1[] = {101, 102, 103, 104, 105, 106, 107, 108, 109, 110};
int rooms_2[] = {201, 202, 203, 204, 205, 206, 207, 208, 209, 210};
char room_1_stat[10][10] = {"Vacant", "Vacant", "Vacant", "Vacant", "Vacant", "Vacant", "Vacant", "Vacant", "Vacant", "Vacant"};
char room_2_stat[10][10] = {"Vacant", "Vacant", "Vacant", "Vacant", "Vacant", "Vacant", "Vacant", "Vacant", "Vacant", "Vacant"};

void check_in() //Checks_in_into_rooms//
{
    int n, f;
    printf("Enter floor no. (1 or 2): ");
    scanf("%d", &f);
    
    if (f==1 || f==2) 
    {
        printf("Enter desired room No. (101 to 110 for floor 1, 201 to 210 for floor 2): \n");
        scanf("%d", &n);

        int* rooms;
        char (*room_stat)[10];

        if (f == 1) 
        {
            rooms = rooms_1;
            room_stat = room_1_stat;
        } 
        else 
        {
            rooms = rooms_2;
            room_stat = room_2_stat;
        }

        for (int i = 0; i < 10; i++) 
        {
            if (rooms[i] == n) {
                if (strcmp(room_stat[i], "Vacant") == 0) {
                    printf("Room %d is booked\n", n);
                    strcpy(room_stat[i], "Booked");
                } else {
                    printf("Room %d is already booked\n", n);
                }
                return;
            }
        }

        printf("Invalid Room Number\n");
    } 
    else 
    {
        printf("Wrong Floor Entered\n");
    }
}

void check_out() //Checks_out_of_the_booked_rooms//
{
    int n; 
    int f;
    printf("Enter the floor no. (1 or 2): ");
    scanf("%d", &f);

    if (f == 1 || f == 2) {
        printf("Enter the room number to check out: ");
        scanf("%d", &n);

        int* rooms;
        char (*room_stat)[10];

        if (f == 1) {
            rooms = rooms_1;
            room_stat = room_1_stat;
        } else {
            rooms = rooms_2;
            room_stat = room_2_stat;
        }
        for (int i = 0; i < 10; i++) {
            if (rooms[i] == n) {
                if (strcmp(room_stat[i], "Booked") == 0) {
                    printf("Checking out of Room %d\n", n);
                    strcpy(room_stat[i], "Vacant");
                } else {
                    printf("Room %d is already vacant\n", n);
                }
                return;
            }
        }
        printf("Invalid Room Number\n");
    } 
    else 
    {
        printf("Wrong Floor Entered\n");
    }
}
                    
void display_rooms() //Displays_Room_Status//
{
    printf("\nFloor 1 - Room Status:\n");
    for (int i = 0; i < 10; i++) 
    {
        printf("Room %d: %s\n", rooms_1[i], room_1_stat[i]);
    }

    printf("\nFloor 2 - Room Status:\n");
    for (int i = 0; i < 10; i++) 
    {
        printf("Room %d: %s\n", rooms_2[i], room_2_stat[i]);
    }
}

//__Main_Program__//
int main() 
{
    int choice;

    while (1) 
    {
        printf("\nPress 1: Check-In\n");
        printf("Press 2: Check-Out\n");
        printf("Press 3: Display Vacant Rooms\n");
        printf("Press 4: Exit Program\n");
        printf("Enter Choice: ");
        scanf("%d", &choice);
        switch (choice) 
        {
        case 1:                                                                                                     
            check_in(); 
            break;
        case 2:
            check_out();
            break;
        case 3:
            display_rooms();
            break;
        case 4:
            printf("Exiting the program.\n");
            return 0;
        default:
            printf("Invalid choice. Please try again.\n");
        }
    }
    return 0;
}
