import firebase from "firebase/app";
import "firebase/firestore";
import "firebase/auth";

const config = {
  apiKey: "AIzaSyAAvY6B5kU2wEW4VuQflawZzCweyJu4Hgo",
  authDomain: "engineering-capstone.firebaseapp.com",
  databaseURL: "https://engineering-capstone.firebaseio.com",
  projectId: "engineering-capstone",
  storageBucket: "engineering-capstone.appspot.com",
  messagingSenderId: "9729553814"
};
const fire = firebase.initializeApp(config);
fire.firestore().settings({ timestampsInSnapshots: true });

export default fire;
