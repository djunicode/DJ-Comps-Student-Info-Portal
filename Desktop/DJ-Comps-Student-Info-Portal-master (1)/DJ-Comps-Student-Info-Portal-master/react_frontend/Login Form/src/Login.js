import React, {Component} from 'react';

export default class Parent extends Component{
	constructor(props){
		super(props)
		this.state=
			{signup: false,
			login: true}
			
	}
	switch(word){
		var signup,login;
		if (word=="signup"){signup=true;login=false;}
		else{login=true;signup=false;}
		return this.setState({login:login,signup:signup})
	}
	render(){
		var self=this;
		return(
			<div>
                      <div id="buttons">
                        <p id="signupButton" onClick={self.switch.bind(null,"signup")} className={self.state.signup ? "yellow":"blue"}>Sign In</p>
                      <p id="loginButton" onClick={this.switch.bind(null,"login")} className={self.state.login ? "yellow":"blue"}> Login</p>
                      </div>
              
                   { self.state.signup?<Signup/> : null}
                   {self.state.login? <Login /> : null}
            
             </div>
        )
	}
}

class Signup extends Component{
  
  
      render(){
      	return (
            <div>
                   
                  <div id="b1">
                        <input type="text" id="first" placeholder="First Name"/>
                        <input type="text" id="last" placeholder="Last Name"/>
                        <input type="email" id="email" placeholder="Email"/>
                    <input type="password" id="password" placeholder="Password"/>
                    <input type="password" id="confirm" placeholder="Confirm Password"/>
                    
            </div>
                </div>
            
            )
      }
}

class Login extends Component{
      render(){
      	return (
            
                  <div>
                              
                 <div id="login">
                    <input type="email" id="email" placeholder="Email"/>
                    <input type="password" id="password" placeholder="Password"/>
 
            </div>
                
                  </div>
              
            )
      }
}
