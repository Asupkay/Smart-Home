import React, { Component } from "react";
import fire from "../config/fire";
import { Panel } from "react-bootstrap";

const divStyle = {
  display: "flex",
  alignItems: "center",
  marginTop: 100,
  marginLeft: 500
};

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

class Login extends Component {
  constructor(props) {
    super(props);
    this.login = this.login.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.signup = this.signup.bind(this);
    this.state = {
      email: "",
      password: ""
    };
  }

  login(e) {
    e.preventDefault();
    fire
      .auth()
      .signInWithEmailAndPassword(this.state.email, this.state.password)
      .then(u => {})
      .catch(error => {
        console.log(error);
      });
  }

  signup(e) {
    e.preventDefault();
    fire
      .auth()
      .createUserWithEmailAndPassword(this.state.email, this.state.password)
      .catch(error => {
        console.log(error);
      });
  }

  handleChange(e) {
    this.setState({ [e.target.name]: e.target.value });
  }

  render() {
    return (
      <div className="col-md-6" style={divStyle}>
        <Panel style={panelStyle}>
          <form>
            <div class="form-group">
              <label for="exampleInputEmail1">Email address</label>
              <input
                value={this.state.email}
                onChange={this.handleChange}
                type="email"
                name="email"
                class="form-control"
                id="exampleInputEmail1"
                placeholder="Enter email"
              />
            </div>
            <div class="form-group">
              <label for="exampleInputPassword1">Password</label>
              <input
                value={this.state.password}
                onChange={this.handleChange}
                type="password"
                name="password"
                class="form-control"
                aria-describedby="passwordHelp"
                id="exampleInputPassword1"
                placeholder="Password"
              />
              <small id="passwordHelp" class="form-text text-muted">
                Password should be 6 characters
              </small>
            </div>
            <button
              type="submit"
              style={buttonStyle}
              onClick={this.login}
              class="btn btn-primary"
            >
              Login
            </button>
            <button
              style={buttonStyle}
              onClick={this.signup}
              style={{ marginLeft: "25px" }}
              className="btn btn-success"
            >
              Signup
            </button>
          </form>
        </Panel>
      </div>
    );
  }
}

export default Login;
