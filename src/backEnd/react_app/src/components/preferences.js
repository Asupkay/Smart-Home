import React from 'react';

const Preferences = (props) => {

  return (
    <nav className="navbar navbar-dark bg-dark">
      <a className="navbar-brand" href="/">
        <p style={{display: 'inline'}}>{ props.title }</p>
      </a>
    </nav>
  )
}

export default Preferences;
