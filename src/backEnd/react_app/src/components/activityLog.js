import React, { Component } from 'react';

class ActivityLog extends Component {
    state = {
      activities: [
                  {
                    time: '10/12/18 10:18', 
                    label: "Alex_Sup", 
                    confidence: .80 
                  }, 
                  {
                    time: '10/12/18 10:18', 
                    label: "John_Banya", 
                    confidence: .60
                  }, 
                  {
                    time: '10/12/18 10:17', 
                    label: "Ruthy_Levi", 
                    confidence: .20
                  }
                ]
    };

  render() { 
    return (
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
            { renderActivities(this.state.activities) }
          </tbody>
        </table>
      </div>
    );
  }
}

const renderActivities = (activities) => {
  if(activities.length === 0) return <p>No Activities</p>
  return <React.Fragment>{ activities.map((activity, index) => <tr key = {index}>
      <th scope="row">{ index }</th>
      <td>{activity.time}</td>
      <td>{activity.label}</td>
      <td>{activity.confidence}</td>
    </tr>) }
  </React.Fragment>
}

export default ActivityLog;
