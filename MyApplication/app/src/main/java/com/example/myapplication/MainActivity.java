package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import androidx.room.Room;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    AppDatabase db;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        db = Room.databaseBuilder(getApplicationContext(),
                        AppDatabase.class, "student-db")
                .allowMainThreadQueries()  // Explain: "Not recommended for real apps, okay for demo"
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
            Log.d("hello", stu.name + " - " + stu.age);

        }

        TextView resultText = findViewById(R.id.resultTextView);
        StringBuilder builder = new StringBuilder();
        for (Student s1 : list) {
            builder.append("ID: ").append(s1.id)
                    .append(" Name: ").append(s1.name)
                    .append(" Age: ").append(s1.age).append("\n");
        }
        resultText.setText(builder.toString());
    }
}
