import React, { useState, useEffect } from 'react';
import { Button } from './Button';
import { Link } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
  const [click, setClick] = useState(false);
  const [button, setButton] = useState(true);

  const closeMobileMenu = () => setClick(false);

  const showButton = () => {
    if (window.innerWidth <= 960) {
      setButton(false);
    } else {
      setButton(true);
    }
  };

  useEffect(() => {
    showButton();
  }, []);

  window.addEventListener('resize', showButton);

  return (
    <>
      <nav className='navbar'>
        <div className='navbar-container'>
          <Link to='/' className='navbar-logo' onClick={closeMobileMenu}>
            <h1>SmartBot</h1>
            <i className='fab fa-typo3' />
          </Link>
          <ul className={click ? 'nav-menu active' : 'nav-menu'}>
            <li className='nav-item'>
              {/* <Link
                to = "/chat"
                className='nav-links'
                onClick={closeMobileMenu}
              >
                Chat
              </Link> */}
              <a className='nav-links' href='http://127.0.0.1:5000/chat'>Chat</a>
            </li>       
            <li className='nav-item'>
              <Link
                to='/AboutUs'
                className='nav-links'
                onClick={closeMobileMenu}
              >
                About SmartBot
              </Link>
            </li>

            <li>
              <Link
                to='/sign-up'
                className='nav-links-mobile'
                onClick={closeMobileMenu}
              >
               Login
              </Link>
            </li>
          </ul>
          {button && <Button buttonStyle='btn--outline'>LOGIN</Button>}
        </div>
      </nav>
    </>
  );
}

export default Navbar;
