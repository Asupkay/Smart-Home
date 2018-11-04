import React, { Component } from 'react';
import NavBar from './components/navBar';
import './App.css';

class App extends Component {
  state = {
    navBarTitle: "Activity Log"
  };


  render() {
    return (
      <div className="App">
        <NavBar title = { this.state.navBarTitle }/>
        <header className="App-header">
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
        </header>
      </div>
    );
  }
}

export default App;
