package com.honor168.relaycontrol;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.SeekBar;
import android.widget.TextView;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.IgnoreExtraProperties;
import com.google.firebase.database.ValueEventListener;

@IgnoreExtraProperties
class RGBLed{
    public int R;
    public int G;
    public int B;

    public RGBLed(){

    }

    public RGBLed(int r, int g, int b){
        R = r;
        G = g;
        B = b;
    }
}

public class RGBActivity extends AppCompatActivity {

    private SeekBar rSeekBar;
    private SeekBar gSeekBar;
    private SeekBar bSeekBar;


    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        switch (item.getItemId()){
            case R.id.sub1:
                Log.d("optionItem","itemClick");
                break;
        }
        return super.onOptionsItemSelected(item);
    }




    private TextView rTextView;
    private TextView gTextView;
    private TextView bTextView;

    private DatabaseReference rgbLedRef = FirebaseDatabase.getInstance().getReference("iot20191126/RGBLed");

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.submenu,menu);
        return super.onCreateOptionsMenu(menu);
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_r_g_b);
        rSeekBar = (SeekBar) findViewById(R.id.redBar);
        gSeekBar = (SeekBar) findViewById(R.id.greenBar);
        bSeekBar = (SeekBar) findViewById(R.id.blueBar);
        rTextView = (TextView) findViewById(R.id.redTextView);
        gTextView = (TextView) findViewById(R.id.greenTextView);
        bTextView = (TextView) findViewById(R.id.blueTextView);
        rTextView.setText("R:" + rSeekBar.getProgress());
        gTextView.setText("G:" + rSeekBar.getProgress());
        bTextView.setText("B:" + rSeekBar.getProgress());
        SeekBar.OnSeekBarChangeListener seekBarlistener = new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                switch (seekBar.getId()) {
                    case R.id.redBar:
                        RGBActivity.this.rTextView.setText("R:" + progress);
                        break;
                    case R.id.greenBar:
                        RGBActivity.this.gTextView.setText("G:" + progress);
                        break;

                    case R.id.blueBar:
                        RGBActivity.this.bTextView.setText("B:" + progress);
                        break;
                    default:
                        break;

                }
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {
            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {
                RGBLed led = new RGBLed(RGBActivity.this.rSeekBar.getProgress(), RGBActivity.this.gSeekBar.getProgress(), RGBActivity.this.bSeekBar.getProgress());
                switch (seekBar.getId()) {
                    case R.id.redBar:
                        Log.d("SeekBar", "red");
                        led.R = seekBar.getProgress();
                        rTextView.setText("R:" + rSeekBar.getProgress());
                        break;
                    case R.id.greenBar:
                        Log.d("SeekBar", "green");
                        led.G = seekBar.getProgress();
                        gTextView.setText("G:" + rSeekBar.getProgress());
                        break;

                    case R.id.blueBar:
                        Log.d("SeekBar", "blue");
                        led.B = seekBar.getProgress();
                        bTextView.setText("B:" + rSeekBar.getProgress());
                        break;
                    default:
                        break;
                }
                RGBActivity.this.rgbLedRef.setValue(led);
            }
        };
        rSeekBar.setOnSeekBarChangeListener(seekBarlistener);
        gSeekBar.setOnSeekBarChangeListener(seekBarlistener);
        bSeekBar.setOnSeekBarChangeListener(seekBarlistener);


        ValueEventListener ledListener = new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                Log.d("firebase", "dataChange");
                RGBLed ledState = dataSnapshot.getValue(RGBLed.class);
                RGBActivity.this.rSeekBar.setProgress(ledState.R);
                RGBActivity.this.gSeekBar.setProgress(ledState.G);
                RGBActivity.this.bSeekBar.setProgress(ledState.B);
                RGBActivity.this.rTextView.setText("R:" + ledState.R);
                RGBActivity.this.gTextView.setText("G:" + ledState.G);
                RGBActivity.this.bTextView.setText("B:" + ledState.B);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        };

        rgbLedRef.addValueEventListener(ledListener);


    }
    public void back (View view){
        finish();
    }

}
