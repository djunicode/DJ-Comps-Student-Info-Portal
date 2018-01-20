import React, { Component } from 'react';
import './App.css';
import TextField from 'material-ui/TextField';	
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import Container from 'muicss/lib/react/container';
import Button from 'muicss/lib/react/button';
import Tabs from 'muicss/lib/react/tabs';
import Tab from 'muicss/lib/react/tab';
import Parent from './Login';
import Signup from './Signup';
class App extends Component {
  render() {
    return (
      <div className="App">
      <MuiThemeProvider>
        <header className="App-header">
          <h1 className="App-title">Log In Form</h1>
        </header>
        <Container className="Con" fluid={true}> 
        <br/><br/><br/>
        <Signup />
        {/*<div class="tab">       
         <button class="tablinks" onclick="openCity(event, 'London')">London</button>
        <button class="tablinks" onclick="openCity(event, 'Paris')">Paris</button>
        </div>
        <div id="London" class="tabcontent">
        <h3>London</h3>
  <p>London is the capital city of England.</p>
</div>

<div id="Paris" class="tabcontent">
  <h3>Paris</h3>
  <p>Paris is the capital of France.</p> 
</div>
{function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}*/}
		<br/><br/><br/>
       
          	
          

         </Container>
	  </MuiThemeProvider>
      </div>
    );
  }
}

export default App;
	