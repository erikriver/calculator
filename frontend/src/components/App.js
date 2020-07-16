import React from 'react';
import Display from './Display';
import Keypad from './Keypad';
import './App.css';

export default class App extends React.Component {
  render() {
    return (
      <div className="app">
          <Display />
          <Keypad />
      </div>
    );
  }
}
