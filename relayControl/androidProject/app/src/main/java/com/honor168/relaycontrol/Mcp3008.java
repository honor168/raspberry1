package com.honor168.relaycontrol;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.widget.ProgressBar;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.IgnoreExtraProperties;
import com.google.firebase.database.ValueEventListener;

@IgnoreExtraProperties
class PWM{
    public int value;
    public PWM(){

    }

    public PWM(int v){
        value = v;
    }
}

public class Mcp3008 extends AppCompatActivity {

    private ProgressBar bar;
    private DatabaseReference pwmReference;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_mcp3008);
        setTitle("可變電阻");

        bar = findViewById(R.id.progressBar);
        bar.setProgress(100);	        //bar.setProgress(100);
        pwmReference = FirebaseDatabase.getInstance().getReference("iot20191126/PWM");
        pwmReference.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                PWM pwm = dataSnapshot.getValue(PWM.class);
                bar.setProgress(pwm.value);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.submenu1,menu);
        return super.onCreateOptionsMenu(menu);
    }

    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        switch (item.getItemId()){
            case R.id.subRGB:
                Log.d("optionItem","itemClick");
                Intent intent = new Intent(this,RGBActivity.class);
                startActivity(intent);
                finish();
        }
        return super.onOptionsItemSelected(item);
    }
}
