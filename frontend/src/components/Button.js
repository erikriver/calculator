import React from "react";
import PropTypes from "prop-types";
import "./Button.css";

export default class Button extends React.Component {
  static propTypes = {
    name: PropTypes.string,
    orange: PropTypes.bool,
    gray: PropTypes.bool,
    large: PropTypes.bool,
  };
  render() {
    const className = [
      "button",
      this.props.orange ? "orange" : "",
      this.props.gray ? "gray" : "",
      this.props.large ? "large" : "",
    ];

    return (
      <div className={className.join(" ").trim()}>
        <button>{this.props.name}</button>
      </div>
    );
  }
}
