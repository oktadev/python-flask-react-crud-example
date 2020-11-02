import React, { Component } from 'react';
import { Switch, Route, BrowserRouter as Router } from 'react-router-dom'
import { Security, LoginCallback, SecureRoute } from '@okta/okta-react';

import Login from '../Login'
import Home from '../Home'

class Main extends Component {
  render() {
    return (
      <Router>
        <Security
          issuer={'https://dev-133320.okta.com/oauth2/default'}
          client_id='0oa66mnfcdMzJuS3n357'
          redirect_uri={window.location.origin + '/implicit/callback'}
          scope={['openid', 'profile', 'email']}>

          <Switch>
            <Route exact path="/" component={Login} />
            <Route path="/implicit/callback" component={LoginCallback} />
            <SecureRoute path="/home" component={Home} />
          </Switch>
        </Security>
      </Router>
    );
  }
}

export default Main;
