import React, { Component } from 'react';
import { Switch, Route, } from 'react-router-dom'
import { Security, ImplicitCallback, SecureRoute } from '@okta/okta-react';

import Login from '../Login'
import Home from '../Home'

class Main extends Component {
  render() {
    return (
      <main>
        <Security 
          issuer={'https://dev-509836.oktapreview.com/oauth2/default'}
          client_id={'0oagcbm1o6GTTB9Da0h7'}
          redirect_uri={'http://localhost:3000/implicit/callback'}
          scope={['openid', 'profile', 'email']}>
          
          <Switch>
            <Route exact path="/" component={Login} />
            <Route path="/implicit/callback" component={ImplicitCallback} />
            <SecureRoute path="/home" component={Home} />
          </Switch>
        </Security>
      </main>
    );
  }
}

export default Main;