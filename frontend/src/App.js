import logo from './logo.svg';
import './App.css';
import React, {useEffect, useState} from 'react';
// import * as pImage from "./start_main";
import Button from "@mui/material/Button";

function buttonNothing() {
  console.log("pick me");
}

function App() {

  function callBackendDemo() {
    return fetch("http://localhost:5001/", {
      method: 'GET'
    }).then(response => response.json()).then((data) => {
      console.log(data);
      setBackendMessage(data['detail']);
    }).catch(error => {
      console.log("Error!");
      console.log(error);
    })
  }

  const [backendMessage, setBackendMessage] = useState('');

  useEffect(() => {
    callBackendDemo();
  }, []);


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Demo App
        </p>
        {backendMessage}
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <Button onClick={buttonNothing} autoFocus>
          Do Nothing
        </Button>
      </header>
    </div>
  );
}

export default App;
