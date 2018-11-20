import { combineReducers } from "redux";
import { firestoreReducer } from "redux-firestore";

const rootReducer = combineReducers({
  firestore: firestoreReducer
});

export default rootReducer;
