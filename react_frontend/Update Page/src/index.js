import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App, {NavBar} from './App';

class Update_Page extends React.Component{
  render(){
    return(
      <div>
        <NavBar />

        <App />
      </div>
    );
  }
}
ReactDOM.render(<Update_Page  />, document.getElementById('root'));
