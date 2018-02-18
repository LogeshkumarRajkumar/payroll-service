import React, { Component } from 'react';
import './Registration.css';
import { Button, FormControl, Label } from 'react-bootstrap';
import axios from 'axios';

class Register extends  Component {
  constructor(){
    super();
    this.state = {
        first_name: '',
        last_name: '',
        email: '',
        company_name: '',
        error_message: '',
        success_message: ''
    };

    this.handleChange = this.handleChange.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
  }

  handleChange(e) {
    this.setState({ [e.target.name]: e.target.value });
  }

  onSubmit(){
      this.setState({error_message: '', success_message: '' });
      axios.defaults.withCredentials = true;
      axios.post('http://127.0.0.1:8000/authentication/register/', {
      headers: { 'Content-Type': 'application/json',
                 },
      name: this.state.company_name,
      creator: { email: this.state.email,
                 first_name: this.state.first_name,
                 last_name: this.state.last_name,
                 password: this.textInput.value
               }
      })
      .then(response => {
        console.log(response);
        this.setState({success_message: 'Thankyou! Verification email has been sent to your registered email'});
      })
      .catch(err => {
        console.log(err);
        this.setState({error_message: 'Sorry! Please Enter Valid Data'});
      });
  }

  render() {
    return (
    <div style={{background: 'mintcream'}}>
      <div className="Register">
         <div>
            <Label className="label"> First Name </Label>
            <FormControl onChange={this.handleChange} name="first_name" className="form-control" placeholder="Enter First name.."></FormControl>
         </div>
         <div>
            <Label className="label"> Last Name </Label>
            <FormControl onChange={this.handleChange} name="last_name" className="form-control" placeholder="Enter last name.."></FormControl>
         </div>
         <div>
            <Label className="label"> Email </Label>
            <FormControl onChange={this.handleChange} name="email" className="form-control" placeholder="Enter valid email-id.."></FormControl>
         </div>
         <div>
            <Label className="label"> Company Name </Label>
            <FormControl onChange={this.handleChange} name="company_name" className="form-control" placeholder="Enter your organisation name.."></FormControl>
         </div>
         <div>
            <Label className="label"> Password </Label>
            <FormControl inputRef={input => this.textInput = input}
                id="Password" label="Password" type="password" className="form-control" placeholder="Strong password please!"/>
         </div>
         <Button onClick={this.onSubmit} className="button" bsStyle="success">Register</Button>
         <div>
             <Label className="error">{this.state.error_message}</Label>
         </div>
         <div>
              <Label className="success">{this.state.success_message}</Label>
         </div>
      </div>
    </div>
    );
  }
}

export default Register;
