import React from 'react';
import './App.css';
import ReactImage from './components/ReactImage';
import Main from './components/FileUpload';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          <code>Upload Rice Image</code>
        </p>
	        <Main />
      </header>
    </div>
  );
}

export default App;

