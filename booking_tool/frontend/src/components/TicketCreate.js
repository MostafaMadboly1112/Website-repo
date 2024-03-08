import React, { Component, useState } from "react";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";
import { Link } from "react-router-dom";
import Container from "@material-ui/core/Container";
import { makeStyles } from "@material-ui/core";

export default function TicketCreate() {
  const btn = { backgroundColor: "violet", fontSize: 60 };
  return (
    <Container>
      <Typography variant="h2" color="primary" align="center" gutterBottom>
        Create A Ticket
      </Typography>
      <form noValidate autoComplete="off">
        <TextField
          label="AVS"
          variant="outlined"
          color="secondary"
          fullWidth
          required
        />
        <TextField
          label="User"
          variant="outlined"
          color="secondary"
          fullWidth
          required
        />
        <TextField
          label="Techniker Data"
          variant="outlined"
          color="secondary"
          fullWidth
          required
        />
      </form>

      <Button
        style={btn}
        onClick={() => console.log("You Clicked me")}
        type="submit"
        color="secondary"
        variant="contained"
      >
        Submit
      </Button>
    </Container>
  );
}
