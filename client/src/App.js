import React, { useState } from 'react';
import Navbar from './components/Navbar';
import './App.css';
import Home from './components/pages/Home';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import SignUp from './components/pages/SignUp';
import Login from './components/pages/Login';
import Tutorial from './components/pages/Tutorial';
import Cards from './components/Cards';
import Cards2 from './components/Cards2';
import Cards3 from './components/Cards3';
import Cards4 from './components/Cards4';
import Chat from './components/pages/Chat';
function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Switch>
          <Route path='/' exact component={Home} />
          <Route path='/sign-up' component={SignUp} />
          <Route path='/login' component={Login} />
          <Route path='/Tutorial' component={Tutorial} />
          <Route path='/Chat' component={Chat} />
          <Route path='/Examples' component={Cards} />
          <Route path='/HowToUse' component={Cards2} />
          <Route path='/AboutUs' component={Cards4} />
          

        </Switch>
      </Router>
    </>
  );
}

export default App;
