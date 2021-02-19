package com.example.kiosk;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import android.util.Log;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void handleText(View v) {
        TextView t = findViewById(R.id.inputField);
        String msg = t.getText().toString();

        // handle AWS IoT publishing here

        // if no message input
        if(msg.compareTo("") == 0) {
            ((TextView)findViewById(R.id.lastMsg)).setText("No Messages Sent");
        }
        
        // else if message input
        else {
            ((TextView)findViewById(R.id.lastMsg)).setText(msg);
            Log.d("info", msg);
            t.setText("");
        }
    }
}