import React from 'react';

const NavBar = (props) => {

  return (
    <nav className="navbar navbar-dark bg-dark">
      <a className="navbar-brand" href="/">
        <p style={{display: 'inline'}}>{ props.title }</p>
      </a>
    </nav>
  )
}

export default NavBar;
