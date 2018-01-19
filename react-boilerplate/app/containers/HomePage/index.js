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
import { Button } from 'antd';
// import messages from './messages';
import LoginModal from '../../components/Login/LoginModal';

const ButtonGroup = Button.Group;

export default class HomePage extends React.PureComponent { // eslint-disable-line react/prefer-stateless-function
  state = { loginVisible: false, signUpVisible: false }

  showModal = (type) => {
    if (type === 'login') {
      this.setState({ loginVisible: true, signUpVisible: false });
    } else {
      this.setState({ loginVisible: false, signUpVisible: true });
    }
  }

  closeModal = (type) => {
    if (type === 'login') {
      this.setState({ loginVisible: false });
    } else {
      this.setState({ signUpVisible: false });
    }
  }

  render() {
    return (
      <div style={{ flexDirection: 'column', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>

        <h1 style={{ fontSize: 60, color: '#cf1322' }}> RUAlumni </h1>

        <ButtonGroup>
          <Button onClick={() => this.showModal('login')}> Log In </Button>
          <Button onClick={() => this.showModal('signup')}> Sign Up </Button>
        </ButtonGroup>

        <LoginModal
          visible={this.state.loginVisible}
          closeModal={this.closeModal}
          showModal={this.showModal}
        />

      </div>
    );
  }
}
