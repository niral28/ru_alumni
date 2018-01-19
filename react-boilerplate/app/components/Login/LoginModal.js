import { Modal, Icon, Divider } from 'antd';
import React from 'react';
import PropTypes from 'prop-types';
import LoginForm from './LoginForm';

export default class App extends React.Component {

  onCancel = () => {
    this.props.closeModal('login');
  }

  handleOk = () => {
    this.props.closeModal('login');
  }

  render() {
    return (
      <div>
        <Modal
          footer={null}
          visible={this.props.visible}
          onOk={this.handleOk}
          onCancel={this.onCancel}
        >
          <div style={{ flexDirection: 'column', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div>
              <Icon type="linkedin" style={{ fontSize: 100, color: '#08c' }} />
            </div>
            <div>
              <Divider> or </Divider>
            </div>
            <div>
              <LoginForm />
            </div>
          </div>
        </Modal>
      </div>
    );
  }
  }

App.propTypes = {
  visible: PropTypes.bool,
  closeModal: PropTypes.func,
};
