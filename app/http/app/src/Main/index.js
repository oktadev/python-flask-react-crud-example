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
          issuer={'https://dev-537985.okta.com/oauth2/default'}
          client_id={'0oacjk9u0weh8u7nr4x6'}
          redirect_uri={'http://localhost:8080/implicit/callback'}
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