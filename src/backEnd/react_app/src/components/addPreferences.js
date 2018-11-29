import React, { Component } from "react";
import fire from "../config/fire";
import { Panel } from "react-bootstrap";

const panelStyle = {
  backgroundColor: "rgba(255,255,255,0.5)",
  border: 0,
  paddingLeft: 20,
  paddingRight: 20,
  width: 300
};

const buttonStyle = {
  marginBottom: 0
};

class AddPreferences extends Component {
  constructor(props) {
    super(props);
    this.addUser = this.addUser.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.state = {
      houseName: "",
      preferences: ""
    };
  }

  handleChange(e) {
    this.setState({ [e.target.name]: e.target.value });
  }

  addUser = e => {
    e.preventDefault();
    const db = fire.firestore();
    db.settings({
      timestampsInSnapshots: true
    });
    const userRef = db.collection("Users").add({
      houseName: this.state.houseName,
      preferences: this.state.preferences
    });
    this.setState({
      houseName: "",
      preferences: ""
    });
  };

  render() {
    return (
      <div className="col-md-6">
        <Panel style={panelStyle}>
          <form>
            <br />
            <div class="form-group">
              <br />
              <p>
                <b>
                  <font size="4">Add your preferences here</font>
                </b>
              </p>
              <label for="exampleInputHouse1">User Name</label>
              <input
                value={this.state.houseName}
                onChange={this.handleChange}
                type="text"
                name="houseName"
                class="form-control"
                id="exampleInputHouse1"
                placeholder="Enter User Name"
              />
            </div>
            <div class="form-group">
              <label for="exampleInputPreferences1">Preference</label>
              <input
                value={this.state.preferences}
                onChange={this.handleChange}
                type="text"
                name="preferences"
                class="form-control"
                id="exampleInputPreferences1"
                placeholder="Enter Preference"
              />
            </div>

            <button type="submit" style={buttonStyle} onClick={this.addUser}>
              Submit
            </button>
          </form>
        </Panel>
      </div>
    );
  }
}

export default AddPreferences;
