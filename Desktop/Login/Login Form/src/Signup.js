import React,{Component} from 'react';
import {Tabs, Tab} from 'material-ui/Tabs';
import TextField from 'material-ui/TextField';
import './App.css';
import Button from 'muicss/lib/react/button';

export default class Signup extends Component{
  constructor(props) {
    super(props);
    this.state = {
      value: 'a',
    };
  }

  handleChange = (value) => {
    this.setState({
      value: value,
    });
  };

  state = {
    passwordDisplayed: false
  }

  toggleDisplay() {
    this.setState({ passwordDisplayed: !this.state.passwordDisplayed })
  }

  render() {
    return (
      <Tabs
        value={this.state.value}
        onChange={this.handleChange}
      >
        <Tab label="Login" value="a">
          <div className="tf">
          <br/><br/>
          <form
                    id="login"
                    action="user_profile/login.html"
                    method="post">
          <TextField
            hintText="Enter your SAP ID"
            floatingLabelText="SAP ID"
            onChange = {(event,newValue) => this.setState({username:newValue})}
          />
          <br/>
        <TextField
            hintText="Enter your Password"
            floatingLabelText="Password"
            onChange = {(event,newValue) => this.setState({password:newValue})}
            type="password"
            id="password"
            />
            </form>
            <br/><br/>
            <Button className="b1">GO!</Button>
            <br/><br/>
            <div className="fyp"><a href="">Forgot your password?</a></div>

            
          </div>
        </Tab>
        <Tab label="Signup" value="b">
          <div>
            <div className="tf">
            <br/><br/>
            <form
                    id="signup"
                    action="user_profile/registration.html"
                    method="post">
              <TextField className="tf"
              hintText="Enter your SAP ID"
              floatingLabelText="SAP ID"
              onChange = {(event,newValue) => this.setState({username:newValue})}
            />
          <br/>
        <TextField className="tf"
            hintText="Enter your Password"
            floatingLabelText="Password"
            onChange = {(event,newValue) => this.setState({password:newValue})}
            type="password"
            /> 
            <br/>            
        <TextField className="tf"
            hintText="Username"
            floatingLabelText="Username"
            onChange = {(event,newValue) => this.setState({password:newValue})}
            /><br/><br/>       
            </form>
            <Button className="b1">Register</Button>      
                     
            </div>
          </div>
        </Tab>
      </Tabs>
    );
  }
}







