import React, { Component } from 'react';
import NavBar from './components/navBar';
import ActivityLog from './components/activityLog';
import './App.css';

class App extends Component {
  state = {
    navBarTitle: "Activity Log",
    activities: [{label: "Alex_Sup", confidence: .80 }, {label: "John_Banya", confidence: .60}, {label: "Ruthy_Levi", confidence: .20}]
  };


  render() {
    return (
      <div className="App">
        <NavBar title = { this.state.navBarTitle }/>
        <ActivityLog activities = { this.state.activities}/>
      </div>
    );
  }
}

export default App;
