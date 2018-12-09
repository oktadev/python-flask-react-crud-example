import React from 'react'
import Button from '@material-ui/core/Button';
import { Redirect } from 'react-router-dom'
import { withAuth } from '@okta/okta-react';

class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = { authenticated: null };
    this.checkAuthentication = this.checkAuthentication.bind(this);
    this.login = this.login.bind(this);
  }

  async checkAuthentication() {
    const authenticated = await this.props.auth.isAuthenticated();
    if (authenticated !== this.state.authenticated) {
      this.setState({ authenticated });
    }
  }

  async componentDidMount() {
    this.checkAuthentication()
  }

  async login(e) {
    this.props.auth.login('/home');
  }

  render() {
    if (this.state.authenticated) {
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

export default withAuth(Login);