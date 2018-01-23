import React, { Component } from 'react';
import {Row,Col} from 'react-bootstrap';
import Logo from '../assets/logo.png';
import '../styles/header.css';

class Header extends Component {
  render() {
    return (
    	<header className="container-fluid">
			<Row bsClass="heading"> 
				<Col xs={6} md={9} lg={10}>
					<img src={Logo} className='logo' />
	    		</Col>
	    		<Col xs={6} md={3} lg={2}>
					<img className="profile_pic1" />
					<span class="glyphicon glyphicon-search search-button"></span>
				</Col>
				
	    	</Row>
    	</header>
    );
  }
}

export default Header;
