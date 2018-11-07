import React from 'react';

const renderBackButton = (location) => {
  if(location !== "Dashboard") {
    return <p style={{display: 'inline'}}>&lt; </p>
  }
}

const NavBar = (props) => {

  return (
    <nav className="navbar navbar-dark bg-dark">
      <a className="navbar-brand" href="/">
        { renderBackButton(props.title) }
        <p style={{display: 'inline'}}>{ props.title }</p>
      </a>
    </nav>
  )
}


export default NavBar;
