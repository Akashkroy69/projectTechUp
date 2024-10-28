struct Student
{
    int id;
    int age;
};

int main(){
    struct Student student1 = {1,20};
    printf("\nid %d age %d\n",student1.id,student1.age);
    struct Student student2;

    student2.id = 2;
    student2.age = 18;
    printf("\nid %d age %d\n",student2.id,student2.age);

    struct Student *student3 = (struct Student*)malloc(sizeof(struct Student));

    student3->id = 3;
    student3->age = 25;
    printf("\nid %d age %d\n",student3->id,student3->age);

    free(student3);

}
