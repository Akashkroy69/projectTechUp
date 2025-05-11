package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import androidx.room.Room;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    AppDatabase db;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        db = Room.databaseBuilder(getApplicationContext(),
                        AppDatabase.class, "student-db")
                .allowMainThreadQueries()
                .build();


        // Inserts student
        Student s = new Student();
        s.name = "Riya";
        s.age = 20;
        db.studentDao().insertStudent(s);

        // Reads all students
        List<Student> list = db.studentDao().getAllStudents();
        for (Student stu : list) {
            System.out.println("hello");
            System.out.println(stu.name + " - " + stu.age);


        }
    }
}
