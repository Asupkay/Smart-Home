import React, { Component } from "react";
import fire from "../config/fire";
import Login from "./Login";
import Home from "./Home";
import NoMatch from "./noMatch";
import { Route, Switch } from "react-router-dom";

class Dashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      user: {}
    };
  }

  componentDidMount() {
    this.authListner();
  }

  authListner() {
    fire.auth().onAuthStateChanged(user => {
      if (user) {
        this.setState({ user });
      } else {
        this.setState({ user: null });
      }
    });
  }

  render() {
    return (
      <div className="Dashboard">
        {this.state.user ? (
          <React.Fragment>
            <Switch>
              <Route path="/activitylog" component={Home} />
              <Route path="/preferences" component={Home} />
              <Route exact path="/" component={Home} />
              <Route component={NoMatch} />
            </Switch>{" "}
          </React.Fragment>
        ) : (
          <React.Fragment>
            <h2>Welcome to your Smart Home</h2>
            <p>
              Please enter your credentials and hit 'Login' if you are a
              returning user or 'Signup' if you are new user
            </p>
            <Login />
          </React.Fragment>
        )}
      </div>
    );
  }
}

export default Dashboard;
