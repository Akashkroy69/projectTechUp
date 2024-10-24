package com.example.fragmentsatcore

import android.content.Context
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment

class FragmentA : Fragment() {

    override fun onAttach(context: Context) {
        super.onAttach(context)
    } //(called before onCreate() of Fragment)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {    // (this is where the fragment inflates its layout)

       val view = inflater.inflate(R.layout.layout_fragment_a, container,false)
        return view
    }
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