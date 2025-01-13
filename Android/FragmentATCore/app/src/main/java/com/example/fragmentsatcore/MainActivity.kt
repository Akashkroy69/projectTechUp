package com.example.fragmentsatcore

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentManager
import androidx.fragment.app.FragmentTransaction

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)


//        dynamically adding fragment
//        step 1: create fragment instance
        val fragmentA = FragmentA()
//        The FragmentManager is responsible for interacting with fragments in your activity.
//        so we need to get a Fragment Manager instance
//        val fragmentManager = FragmentManager()
//        but the Fragment Manager class is an abstract class, so we need to get the instance
//        of its concrete class which is FragmentManagerImpl

        val fragmentManager = FragmentManager.findFragment<>()
        val transaction = supportFragmentManager.beginTransaction()

    }
}