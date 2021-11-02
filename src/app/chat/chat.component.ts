import { Component, OnInit } from '@angular/core';

import * as moment from 'moment';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss']
})
export class ChatComponent implements OnInit {

  messages: Message[] = [];

  messageText: string;

  constructor() {}

  ngOnInit() {
    this.messages.push({ name: 'Claudio', receiver: true, hour: '14:01', text: 'Bom dia, tudo bem?' });
  }

  onSend() {
    this.messages.push({ name: 'Vitor', receiver: false, hour: moment().format('HH:mm'), text: this.messageText });
    this.messageText = null;
  }
}

interface Message {
  name: string;
  hour: string;
  text: string;
  receiver: boolean;
}
