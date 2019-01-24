import React, { Component } from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import AddPreferences from "./addPreferences";
import DisplayPreferences from "./displayPreferences";

class Preferences extends Component {
  render() {
    return (
      <Router>
        <div>
          <p>
            <b>
              <font size="5">Preferences</font>
            </b>
          </p>
          <ul>
            <li>
              <Link to="/addPreferences">Add Preferences</Link>
            </li>
            <li>
              <Link to="/displayPreferences">Display Preferences</Link>
            </li>
          </ul>

          <Route exact path="/addPreferences" component={AddPreferences} />
          <Route
            exact
            path="/displayPreferences"
            component={DisplayPreferences}
          />
        </div>
      </Router>
    );
  }
}

export default Preferences;
