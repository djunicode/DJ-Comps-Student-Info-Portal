import React from 'react';
import './App.css';
import ExpansionPanel, {
  ExpansionPanelSummary,
  ExpansionPanelDetails,
} from 'material-ui/ExpansionPanel';
import TextField from 'material-ui/TextField';
import Button from 'material-ui/Button';


class App extends React.Component {
  constructor(props){
  super(props);
  this.state = {
    expanded: null,


};

  this.handleExpansion=this.handleExpansion.bind(this);
}


  handleExpansion = panel => (event, expanded ) => {
    this.setState({
      expanded: expanded ? panel : false,

    });
  }

  render() {

    return (
      <div >
        <div className="Dropdowns">
       <ExpansionPanel expanded={this.state.expanded === 'panel1'} onChange={this.handleExpansion('panel1')}>
        <ExpansionPanelSummary>
         Personal Details
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>

         <div class="container">
           <form>
          Name&nbsp;&nbsp;
          <TextField/><br/>
          SAP&nbsp;&nbsp;
          <TextField/><br/>
          Email Id&nbsp;&nbsp;
          <TextField/>
          <br/>
          Mobile No.&nbsp;&nbsp;
          <TextField/><br/>
          Bio&nbsp;&nbsp;
          <TextField/><br/>
          Date of Birth&nbsp;&nbsp;
          <TextField/><br/>
          Skills&nbsp;&nbsp;
          <TextField/><br/>
          Department&nbsp;&nbsp;
          <TextField/><br/>




         </form>
       </div>
        </ExpansionPanelDetails>
       </ExpansionPanel>
       <ExpansionPanel expanded={this.state.expanded === 'panel2'} onChange={this.handleExpansion('panel2')}>
        <ExpansionPanelSummary>
          Skills
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
        <form>
        <TextField placeholder="Descibe your skills "/>

        </form>
        </ExpansionPanelDetails>
       </ExpansionPanel>
       <ExpansionPanel expanded={this.state.expanded === 'panel3'} onChange={this.handleExpansion('panel3')}>
        <ExpansionPanelSummary>

            Internships
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
        <form>
        Company Name&nbsp;&nbsp;
        <TextField id="right"/>
        Position&nbsp;&nbsp;
        <TextField/>
        What did you work on&nbsp;&nbsp;
        <TextField/>

        </form>
        </ExpansionPanelDetails>
       </ExpansionPanel>
       <ExpansionPanel expanded={this.state.expanded === 'panel4'} onChange={this.handleExpansion('panel4')}>
        <ExpansionPanelSummary>
          Projects
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
        <form>
          Name&nbsp;&nbsp;
         <TextField/>&nbsp;&nbsp;
         Description&nbsp;&nbsp;
         <TextField/>&nbsp;&nbsp;
         Mentor(if any)&nbsp;&nbsp;
         <TextField/>
        </form>

        </ExpansionPanelDetails>
       </ExpansionPanel>
       <ExpansionPanel expanded={this.state.expanded === 'panel5'} onChange={this.handleExpansion('panel5')}>
        <ExpansionPanelSummary>
          Hackathon
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
         <form>
         Name&nbsp;&nbsp;
         <TextField/>&nbsp;&nbsp;
         Date&nbsp;&nbsp;
         <TextField/>&nbsp;&nbsp;
         Decribe what you worked on&nbsp;&nbsp;
         <TextField/>
         </form>
        </ExpansionPanelDetails>
       </ExpansionPanel>
       <ExpansionPanel expanded={this.state.expanded === 'panel6'} onChange={this.handleExpansion('panel6')}>
        <ExpansionPanelSummary>
          Committee and Volunteer Work
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
         <form>
         Committee's you're a part of : &nbsp;&nbsp;
         <TextField/>&nbsp;&nbsp;
         Any volunteer work you've undertaken : &nbsp;&nbsp;
         <TextField/>
         </form>
        </ExpansionPanelDetails>
       </ExpansionPanel>
       <ExpansionPanel expanded={this.state.expanded === 'panel7'} onChange={this.handleExpansion('panel7')}>
        <ExpansionPanelSummary>
          Education
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
         <form>
           10th Grade
           <br/><br/>
         <TextField placeholder="School Name"/>&nbsp;&nbsp;
         <TextField placeholder="Board Percentage"/>
           <br/><br/>
           12th Grade
           <br/><br/>
         <TextField placeholder="College Name"/>&nbsp;&nbsp;
         <TextField placeholder="Board Percentage"/>
         </form>
        </ExpansionPanelDetails>
       </ExpansionPanel>
       <ExpansionPanel expanded={this.state.expanded === 'panel8'} onChange={this.handleExpansion('panel8')}>
        <ExpansionPanelSummary>
          Research Papers
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
         <form>
          Title&nbsp;&nbsp;
         <TextField/>
         Description&nbsp;&nbsp;
         <TextField/><br/><br/>
         Publication&nbsp;&nbsp;
         <TextField/>
         Date of Publication&nbsp;&nbsp;
         <TextField/>
         </form>
        </ExpansionPanelDetails>
       </ExpansionPanel>
       <ExpansionPanel expanded={this.state.expanded === 'panel9'} onChange={this.handleExpansion('panel9')}>
        <ExpansionPanelSummary>
          BE Project
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
         <form>
           Name&nbsp;&nbsp;
         <TextField/>&nbsp;&nbsp;
          Description&nbsp;&nbsp;
          <TextField/>&nbsp;&nbsp;
          Mentor&nbsp;&nbsp;
          <TextField/>
         </form>
        </ExpansionPanelDetails>
       </ExpansionPanel>
       <br/>
      </div>
       <Button raised color="primary">
        Submit
       </Button>

      </div>
    );
  }
}

export class NavBar  extends React.Component{
  render(){
    return(
        <div className="Nav">
         <img id="Unicode-Logo" src="" alt="Unicode logo" />
        </div>

);
}
}

export default App;
