import Button from "./Button";
import React from "react";
//import PropTypes from "prop-types";

import "./Keypad.css";

export default class Keypad extends React.Component {

  render() {
    return (
      <div className="keypad">
        <div>
          <Button name="7" />
          <Button name="8" />
          <Button name="9" />
          <Button name="/" orange />
        </div>
        <div>
          <Button name="4" />
          <Button name="5" />
          <Button name="6" />
          <Button name="x" orange />
        </div>
        <div>
          <Button name="1" />
          <Button name="2" />
          <Button name="3" />
          <Button name="+" orange />
        </div>
        <div>
          <Button name="C" gray />
          <Button name="0" />
          <Button name="." />
          <Button name="-" orange />
        </div>
        <div>
          <Button name="=" large orange />
        </div>
      </div>
    );
  }
}
