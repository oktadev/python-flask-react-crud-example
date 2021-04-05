import React from 'react'
import Button from '@material-ui/core/Button';
import { Redirect } from 'react-router-dom'
import { withOktaAuth } from '@okta/okta-react';

class Login extends React.Component {
  constructor(props) {
    super(props);
    this.login = this.login.bind(this);
  }

  async login() {
    await this.props.oktaAuth.signInWithRedirect();
  }

  render() {
    if (this.props.authState.isAuthenticated) {
      return <Redirect to='/home' />
    } else {
      return (
        <div style={{height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
          <Button variant="contained" color="primary" onClick={this.login}>Login with Okta</Button>
        </div>
      )
    }
  }
}

export default withOktaAuth(Login);
