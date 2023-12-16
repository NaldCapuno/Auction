import sys
import tkinter as tk
from python_banyan.banyan_base import BanyanBase


class EchoServer(BanyanBase):
    def __init__(self):
        super(EchoServer, self).__init__(process_name='Server')

        self.set_subscriber_topic('echo')

        try:
            self.receive_loop()
        except KeyboardInterrupt:
            self.clean_up()
            sys.exit(0)

    def incoming_message_processing(self, topic, payload):
        self.publish_payload('Message received in server', 'reply')
        print(payload, 'is ready...')


def echo_server():
    EchoServer()


if __name__ == '__main__':
    echo_server()
