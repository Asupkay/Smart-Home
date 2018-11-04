import React from 'react';

const ActivityLog = (props) => {

  return (
    <div className="container">
      { renderActivities(props.activities) }
    </div>
  )
}

const renderActivities = (activities) => {
  if(activities.length === 0) return <p>No Activities</p>
  return <React.Fragment>{ activities.map(activity => <p>{activity.label} walked in with a confidence of {activity.confidence}</p>) }</React.Fragment>
}

export default ActivityLog;
