import React, { Component } from "react";
import TicketCreate from "./TicketCreate";
import TicketSearch from "./TicketSearch";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <Routes>
          <Route path="/" element={<p>This is the home page</p>} />
          <Route path="/search" element={<TicketSearch />} />
          <Route path="/create" element={<TicketCreate />} />
        </Routes>
      </Router>
    );
  }
}
