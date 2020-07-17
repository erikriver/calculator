import React from "react";
import Display from "./Display";
import Keypad from "./Keypad";
import calculator from "../helpers/controller";

import "./App.css";

export default class App extends React.Component {
  // Using the state with tree elements to control de operations and results
  state = {
    total: null,
    next: null,
    operation: null,
  };

  // for each click on the keypad we call the calculator
  handleClick = (buttonName) => {
    calculator(this.state, buttonName).then((nextState) => {
      console.log(nextState);
      this.setState(nextState);
    });
  };

  render() {
    return (
      <div className="app">
        <Display value={this.state.next || this.state.total || "0"} />
        <Keypad clickHandler={this.handleClick} />
      </div>
    );
  }
}
