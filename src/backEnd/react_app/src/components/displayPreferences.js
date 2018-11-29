import React, { Component } from "react";
import { connect } from "react-redux";
import { firestoreConnect } from "react-redux-firebase";
import { compose } from "redux";

class DisplayPreferences extends Component {
  render() {
    console.log(this.props.Users);

    //const { users } = this.props.Users;
    if (this.props.Users !== undefined) {
      //console.log("win");

      return (
        <div className="container">
          <br />
          <p>
            <b>
              <font size="4">Your Preferences</font>
            </b>
          </p>
          <table className="table">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">ID</th>
                <th scope="col">User</th>
                <th scope="col">Preference</th>
              </tr>
            </thead>
            <tbody>{userPreferences(this.props.Users)}</tbody>
          </table>
        </div>
      );
    }
    return (
      <div>
        <p>Establishing connection with the database..</p>
      </div>
    );
  }
}

const userPreferences = Users => {
  if (Users.length === 0) return <p>No Preferences</p>;
  return (
    <React.Fragment>
      {Users.map((preferences, index) => (
        <tr key={index}>
          <th scope="row">{index + 1}</th>
          <td>{preferences.id}</td>
          <td>{preferences.houseName}</td>
          <td>{preferences.preferences}</td>
        </tr>
      ))}
    </React.Fragment>
  );
};

const mapStateToProps = state => {
  console.log(state);
  //console.log(Object.values(state));
  //console.log(state.firestore.ordered.houses);
  //console.log(this.state.data);

  return {
    Users: state.firestore.ordered.Users
  };
};

export default compose(
  connect(mapStateToProps),
  firestoreConnect([{ collection: "Users" }])
)(DisplayPreferences);
