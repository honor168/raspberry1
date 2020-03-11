package com.honor168.relaycontrol;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;   //
import com.google.firebase.auth.FirebaseUser;   //
import com.google.firebase.firestore.DocumentChange;
import com.google.firebase.firestore.EventListener;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.FirebaseFirestoreException;
import com.google.firebase.firestore.QueryDocumentSnapshot;
import com.google.firebase.firestore.QuerySnapshot;

public class MainActivity extends AppCompatActivity {
    private FirebaseAuth mAuth;     //
    FirebaseFirestore firestore = FirebaseFirestore.getInstance();  //2
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mAuth = FirebaseAuth.getInstance(); //

        /*
        firestore.collection("Doors").get().addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() { //2
            @Override
            public void onComplete(@NonNull Task<QuerySnapshot> task) {
                if(task.isSuccessful()){
                    for (QueryDocumentSnapshot document : task.getResult()) {
                        Log.d("Firestore", document.getId() + " => " + document.getData());
                    }
                }else{
                    Log.d("Firestore", "firestore read fails");
                }
            }
        });
        */

        firestore.collection("Doors").addSnapshotListener(new EventListener<QuerySnapshot>() {
            @Override
            public void onEvent(@Nullable QuerySnapshot snapshots, @Nullable FirebaseFirestoreException e) {
                if(e !=null){
                    Log.d("listener","listener err",e);
                    return;
                }

                for(DocumentChange dc:snapshots.getDocumentChanges()){
                    switch(dc.getType()){
                        case ADDED:
                            Log.d("listener","add:" + dc.getDocument().getData());
                            break;
                        case REMOVED:
                            Log.d("listener","removed:" + dc.getDocument().getData());
                            break;
                        case MODIFIED:
                            Log.d("listener","modified:" + dc.getDocument().getData());
                            break;
                    }
                }

            }
        });
    }

    @Override
    protected void onStart() {
        super.onStart();
        FirebaseUser currentUser = mAuth.getCurrentUser();
        if (currentUser == null){
            Log.d("Login","no login");
            mAuth.signInAnonymously();
        }else{
            Log.d("Login","logined");
            Log.d("Login",currentUser.getUid());
        }
    }
}
