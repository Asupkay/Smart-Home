import firebase from 'firebase/app';
import 'firebase/firestore';
const config = {
    apiKey: "AIzaSyAAvY6B5kU2wEW4VuQflawZzCweyJu4Hgo",
    authDomain: "engineering-capstone.firebaseapp.com",
    databaseURL: "https://engineering-capstone.firebaseio.com",
    projectId: "engineering-capstone",
    storageBucket: "engineering-capstone.appspot.com",
    messagingSenderId: "9729553814"
};

if (!firebase.apps.length) {
    firebase.initializeApp(config);

}

export default firebase;
