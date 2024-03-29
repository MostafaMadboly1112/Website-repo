import React, { Component, useState } from "react";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";
import { Link } from "react-router-dom";
import Container from "@material-ui/core/Container";
import { DemoContainer } from "@mui/x-date-pickers/internals/demo";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { DateTimePicker } from "@mui/x-date-pickers/DateTimePicker";

export default function TicketCreate() {
  const btn = { backgroundColor: "lightblue", fontSize: 20 };
  const field = { marginTop: 20, marginBottom: 20, display: "block" };
  const [value, setValue] = useState(null);
  console.log(value);
  const [avs, setAVS] = useState("");
  const [user, setUSER] = useState("");
  const [tec, setTEC] = useState("");
  const [avsError, setAVSError] = useState(false);
  const [userError, setUSERError] = useState(false);
  const [tecError, setTECError] = useState(false);
  const handleSubmit = (e) => {
    e.preventDefault();
    setAVSError(false);
    setUSERError(false);
    setTECError(false);
    if (avs == "") {
      setAVSError(true);
    }
    if (user == "") {
      setUSERError(true);
    }
    if (tec == "") {
      setTECError(true);
    }

    if (avs && user && tec && from) {
      console.log(avs, user, tec);
    }
  };
  return (
    <Container>
      <Typography variant="h2" color="primary" align="center" gutterBottom>
        Create A Ticket
      </Typography>
      <form noValidate autoComplete="off" onSubmit={handleSubmit}>
        <TextField
          onChange={(e) => setAVS(e.target.value)}
          style={field}
          label="AVS"
          variant="outlined"
          color="secondary"
          fullWidth
          required
          error={avsError}
        />
        <TextField
          onChange={(e) => setUSER(e.target.value)}
          style={field}
          label="User"
          variant="outlined"
          color="secondary"
          fullWidth
          required
          error={userError}
        />
        <LocalizationProvider dateAdapter={AdapterDayjs}>
          <DemoContainer components={["DateTimePicker"]}>
            <DateTimePicker
              label="Booking from"
              value={value}
              onChange={(newValue) => setValue(newValue)}
              slotProps={{ textField: { variant: "outlined" } }}
            />
          </DemoContainer>
        </LocalizationProvider>
        <LocalizationProvider dateAdapter={AdapterDayjs}>
          <DemoContainer components={["DateTimePicker"]}>
            <DateTimePicker label="Booking to" />
          </DemoContainer>
        </LocalizationProvider>
        <TextField
          onChange={(e) => setTEC(e.target.value)}
          style={field}
          label="Techniker Data"
          variant="outlined"
          color="secondary"
          fullWidth
          required
          error={tecError}
        />
        <Button style={btn} type="submit" color="secondary" variant="contained">
          Submit
        </Button>
      </form>
    </Container>
  );
}
