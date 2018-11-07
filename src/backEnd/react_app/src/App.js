import React, { Component } from 'react';
import { Route, Switch, withRouter } from 'react-router-dom';
import './App.css';
import NavBar from './components/navBar';
import ActivityLog from './components/activityLog';
import Preferences from './components/preferences';
import Dashboard from './components/dashboard';
import NoMatch from './components/noMatch';

class App extends Component {
  getTitle = (path) => {
    const pathToTitle = {
      '/activitylog': 'Activity Log',
      '/preferences': 'Preferences',
      '/': 'Dashboard'
    };
    if(pathToTitle[path] === undefined) {
      return '404';
    }  
    return pathToTitle[path];
  }

  render() {
    return (
      <div className="App">
        <NavBar title = { this.getTitle(this.props.location.pathname) }/>
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

export default withRouter(App);
