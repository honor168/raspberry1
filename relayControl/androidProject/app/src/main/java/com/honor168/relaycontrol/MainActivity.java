package com.honor168.relaycontrol;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class MainActivity extends AppCompatActivity {
    private static final String TAG = "RELAYTest";
    private FirebaseDatabase database = FirebaseDatabase.getInstance();
    private DatabaseReference relayRef = database.getReference("iot20191126/ledState");
    private boolean relayCurrentState;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Log.d(TAG, "onCreate");
        relayRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                relayCurrentState = dataSnapshot.getValue(boolean.class);
                Log.d(TAG, relayCurrentState ? "True": "False");
                ImageButton relayButton = (ImageButton) findViewById(R.id.relayButton);

                if (relayCurrentState) {
                    //relayButton.setText("CLOSE");
                    relayButton.setImageResource(R.drawable.open);
                } else{
                    //relayButton.setText("OPEN");
                    relayButton.setImageResource(R.drawable.close);
                }

            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });
    }

    @Override
    protected void onStart() {
        super.onStart();
        Log.d(TAG, "onStart");
    }

    @Override
    protected void onResume() {
        super.onResume();
        Log.d(TAG, "onResume");
    }

    @Override
    protected void onPause() {
        super.onPause();
        Log.d(TAG,"onPause()");
    }

    @Override
    protected void onStop() {
        super.onStop();
        Log.d(TAG,"onStop()");
    }

    @Override
    protected void onRestart() {
        super.onRestart();
        Log.d(TAG,"reStart()");
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Log.d(TAG,"onDestroy()");
    }

    public void user_click(View clickButton){


        relayCurrentState = !relayCurrentState;

        ImageButton btn = (ImageButton) clickButton;
        if(relayCurrentState ){
            btn.setImageResource(R.drawable.open);

        }else {
            btn.setImageResource(R.drawable.close);
        }
        relayRef.setValue(relayCurrentState);
    }

    public void goToRGB(View view) {
        Intent intent = new Intent(this, RGBActivity.class);
        startActivity(intent);
    }
}