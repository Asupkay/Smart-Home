import React, { Component } from 'react';
import { Route, Switch } from 'react-router-dom';
import './App.css';
import NavBar from './components/navBar';
import ActivityLog from './components/activityLog';
import Preferences from './components/preferences';
import Dashboard from './components/dashboard';
import NoMatch from './components/noMatch';

class App extends Component {
  state = {
    navBarTitle: "Activity Log",
    
  };


  render() {
    return (
      <div className="App">
        <NavBar title = { this.state.navBarTitle }/>
        <Switch>
          <Route path='/activitylog' component={ ActivityLog } />
          <Route path='/preferences' component={ Preferences } />
          <Route exact path='/' component={ Dashboard } />
          <Route component={ NoMatch } />
        </Switch>
      </div>
    );
  }
}

export default App;
