import React, { Component } from "react";
import fire from "../config/fire";
import { Panel } from "react-bootstrap";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import Preferences from "./preferences";
import ActivityLog from "./activityLog";

const divStyle = {
  display: "flex",
  alignItems: "center",
  marginTop: 100,
  marginLeft: 200
};

const panelStyle = {
  backgroundColor: "rgba(255,255,255,0.5)",
  border: 0,
  paddingLeft: 20,
  paddingRight: 20,
  width: 300
};

class Home extends Component {
  logout() {
    fire.auth().signOut();
  }

  render() {
    return (
      <div className="col-md-6" style={divStyle}>
        <Panel style={panelStyle} />
        <form>
          <div>
            <h1>Dashboard</h1>
          </div>
          <br />

          <Router>
            <div>
              <ul>
                <li>
                  <Link to="/activitylog">Activity Log</Link>
                </li>
                <li>
                  <Link to="/preferences">Preferences</Link>
                </li>
              </ul>

              <hr />

              <Route exact path="/activitylog" component={ActivityLog} />
              <Route exact path="/preferences" component={Preferences} />
            </div>
          </Router>
          <div>
            <button
              onClick={this.logout}
              style={{
                position: "relative",
                left: 600,
                right: 0,
                top: -250,
                bottom: 0
              }}
            >
              {" "}
              Logout{" "}
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default Home;
