import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./components/App";

ReactDOM.render(
  /* 
  StrictMode is a feature aimed to help us in finding potential problems
  in this application
  */
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
