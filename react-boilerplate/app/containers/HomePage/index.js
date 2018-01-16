/*
 * HomePage
 *
 * This is the first thing users see of our App, at the '/' route
 *
 * NOTE: while this component should technically be a stateless functional
 * component (SFC), hot reloading does not currently support SFCs. If hot
 * reloading is not a necessity for you then you can refactor it and remove
 * the linting exception.
 */

import React from 'react';
// import { FormattedMessage } from 'react-intl';
import { Divider, Icon } from 'antd';
// import messages from './messages';

import LoginForm from '../../components/LoginForm';


export default class HomePage extends React.PureComponent { // eslint-disable-line react/prefer-stateless-function
  render() {
    return (
      <div style={{ flexDirection: 'column', display: 'flex', 'justify-content': 'center', 'align-items': 'center' }}>
        {/* <h1>
          <FormattedMessage {...messages.header} />
        </h1> */}
        <Icon type="linkedin" style={{ fontSize: 100, color: '#08c' }} />
        <Divider> OR </Divider>
        <LoginForm />


      </div>
    );
  }
}
