import React, { Component } from "react";
import { render } from "react-dom";
// import HomePage from "./HomePage";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return <h1>Test React Code</h1>;
    // return (
    //   <div>
    //     <HomePage />
    //   </div>
    // );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
