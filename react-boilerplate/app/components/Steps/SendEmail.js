import React from 'react';
import { Input, Icon } from 'antd';
import './SendEmail.css';

export default class SendEmail extends React.Component {
  state = { validEmail: false }

  // TODO: front-end validate email and then make button clickable and then send the email 

  render() {
    return (
      <div className="send-email">
        <div>
          <Icon style={{ fontSize: 35 }} type="mail" />
        </div>
        <div>
          <p>
            Please input your Rutgers email below to verify you are a Rutgers alumni/student.
            A verification code will be sent to your email.
          </p>
        </div>
        <div>
          <Input placeholder="henry@rutgers.edu" />
        </div>
      </div>
    );
  }
}
