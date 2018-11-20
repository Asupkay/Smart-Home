import React, { Component } from "react";
import fire from "../config/fire";

class ActivityLog extends Component {
  state = {
    activities: []
  };

  componentDidMount(props) {
    const db = fire.firestore();
    const settings = { timestampsInSnapshots: true };
    db.settings(settings);
    const doc = db.collection("activities").doc("houseA");
    const observer = doc.onSnapshot(
      docSnapshot => {
        console.log(
          docSnapshot._document.data.internalValue.root.value.internalValue
        );
        this.setState({
          activities: docSnapshot._document.data.internalValue.root.value.internalValue.sort(
            (a, b) => {
              return (
                b.internalValue.root.right.value.internalValue.seconds -
                a.internalValue.root.right.value.internalValue.seconds
              );
            }
          )
        });
      },
      err => {
        console.log(`Encountered error: ${err}`);
      }
    );
  }

  render() {
    return (
      <React.Fragment>{renderActivities(this.state.activities)}</React.Fragment>
    );
  }
}

const renderActivities = activities => {
  if (activities.length === 0) return <p>No Activities</p>;
  return (
    <React.Fragment>
      <div className="container">
        <table className="table">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Time</th>
              <th scope="col">Name</th>
              <th scope="col">Confidence</th>
            </tr>
          </thead>
          <tbody>
            {activities.map((activity, index) => (
              <tr key={index}>
                <th scope="row">{index}</th>
                <td>
                  {new Date(
                    activity.internalValue.root.right.value.internalValue.seconds
                  ).toLocaleString()}
                </td>
                <td>
                  {activity.internalValue.root.value.internalValue
                    .split("_")
                    .join(" ")}
                </td>
                <td>{activity.internalValue.root.left.value.internalValue}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </React.Fragment>
  );
};

export default ActivityLog;
