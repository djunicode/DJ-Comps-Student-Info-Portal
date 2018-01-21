import React, { Component } from 'react';
import Header from './Header.js';
import { Grid,Row,Col } from 'react-bootstrap';
import '../styles/profile_page.css';
import profilePic from '../assets/profile1.jpg';

const containerStyle = {backgroundColor:'white',padding:'0px',margin:'0px',overflow:'hidden'};

class ProfilePage extends Component {

  render(){
    return (
    	<Grid bsClass="container-fluid" style={containerStyle}>
    		<Header/>
    		<Row bsClass="boundary_none">
    			<Col bsClass="boundary_none" xs={12}>
	    		</Col>
	    	</Row>

	    	<Row bsClass="profile_div">
	    		<Col xs={4} md={3} lg={3}>
	    			<div>
	    				<img className="profile_pic" />
	    			</div>
	    		</Col>
	    		<Col xs={8} md={9} lg={9}>
	    			<h1 className="profile_name">Name</h1><br/><br/><br/><br/><br/>
	    			<button className="add_button">&#x0002B;</button>
	    		</Col>
	    	</Row>

	    	<Row bsClass="info_div">
	    		<Col  sm={4} md={3}>
	    			<ul className="profile_statistics">
	    				<li>Skills<span>13</span></li>
	    				<li>Internships<span>3</span></li>
	    				<li>Research Papers<span>2</span></li>
	    				<li>Competitions<span>6</span></li>
	    				<li>C.G.P.A.<span>8.9</span></li>
	    				<li>Co-curriculum<span>3</span></li>
	    			</ul>
	    		</Col>

	    		<Col sm={4} md={9}>
	    			<div className="content_div">
	    				<Row>
	    					<Col xs={12}>
	    						<div className="summary_div">
	    							<h3>Summary</h3>
	    							
	    							<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc mattis enim ut tellus elementum sagittis vitae. Tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras. Quam viverra orci sagittis eu volutpat odio. Purus ut faucibus pulvinar elementum. Arcu cursus vitae congue mauris rhoncus aenean vel elit. Sit amet purus gravida quis blandit turpis cursus in hac. Et tortor at risus viverra. Felis eget nunc lobortis mattis aliquam faucibus purus in massa. Non diam phasellus vestibulum lorem sed risus ultricies tristique. Dictum varius duis at consectetur lorem donec massa sapien faucibus. Sollicitudin tempor id eu nisl nunc mi ipsum faucibus. Diam volutpat commodo sed egestas egestas. Orci nulla pellentesque dignissim enim sit amet venenatis. Blandit libero volutpat sed cras ornare arcu dui vivamus. Sem nulla pharetra diam sit amet nisl suscipit. Massa tempor nec feugiat nisl pretium fusce id. Donec ac odio tempor orci dapibus ultrices. Pharetra diam sit amet nisl. Orci nulla pellentesque dignissim enim sit amet venenatis.
	    							</p>

	    						</div>
	    					</Col>
	    				</Row>
	    				<Row>
	    					<Col xs={12}>
	    						<div className="work_history_div">
	    							<h3>Work History</h3>

	    							<p>
Vestibulum sed arcu non odio euismod lacinia at quis. Arcu dui vivamus arcu felis bibendum ut. Suspendisse sed nisi lacus sed viverra. Vitae congue mauris rhoncus aenean vel elit scelerisque. Faucibus a pellentesque sit amet porttitor. Nec feugiat nisl pretium fusce id velit. Massa massa ultricies mi quis hendrerit dolor. Vel risus commodo viverra maecenas accumsan lacus. Erat imperdiet sed euismod nisi porta lorem. Eget felis eget nunc lobortis. Ut enim blandit volutpat maecenas volutpat blandit aliquam. Tempus urna et pharetra pharetra massa massa ultricies mi. Ut lectus arcu bibendum at varius vel pharetra vel turpis. Integer enim neque volutpat ac tincidunt. Vitae semper quis lectus nulla at volutpat.
	    							</p>

	    						</div>
	    					</Col>
	    				</Row>

	    			</div>
	    		</Col>
	    	</Row>
    	</Grid>
    );
  }
}

export default ProfilePage;
