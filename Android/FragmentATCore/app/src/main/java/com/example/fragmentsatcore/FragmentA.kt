package com.example.fragmentsatcore

import androidx.fragment.app.Fragment

class FragmentA : Fragment() {

    fun onAttach(){} //(called before onCreate() of Fragment)
    fun onCreate(){}
    fun onCreateView(){}  // (this is where the fragment inflates its layout)
    fun onActivityCreated(){} //(called once the activity's onCreate() method has completed)
    override fun onStart(){
        super.onStart()
    }
    override fun onResume(){
        super.onResume()
    }
    override fun onPause(){
        super.onPause()
    }
    override fun onStop(){
        super.onStop()
    }
    override fun onDestroyView(){
        super.onDestroyView()
    } //(removes the view but keeps fragment object)
    override fun onDestroy(){
        super.onDestroy()
    }
    override fun onDetach(){
        super.onDetach()
    }

}