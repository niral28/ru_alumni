import React from 'react';
import { Modal } from 'antd';
import PropTypes from 'prop-types';
import SignupForm from './SignupForm';

export default class SignupModal extends React.Component {

  onCancel = () => {
    this.props.closeModal('signup');
  }

  handleOk = () => {
    this.props.closeModal('signup');
  }

  render() {
    return (
      <Modal
        footer={null}
        visible={this.props.visible}
        onOk={this.handleOk}
        onCancel={this.onCancel}
      >
        <SignupForm />
      </Modal>
    );
  }
}

SignupModal.propTypes = {
  visible: PropTypes.bool,
  closeModal: PropTypes.func,
};
