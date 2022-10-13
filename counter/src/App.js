import React, { Component } from 'react';
import './App.css';
import Counter from './counter';

class App extends Component{
  render() {
    return (
      <div className="App">
            <h1>Please press the button below</h1>
      <Counter />
      </div>
    );
  }
}

export default App;
