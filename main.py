import inquirer
from inquirer.themes import GreenPassion
import socket

HOST = '127.0.0.1'
PORT = 65436


def request(op, value=None):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(bytes(str((op, value)), encoding='utf8'))
        data = s.recv(1024).decode('utf8')

    print(data)


if __name__ == '__main__':
    question = [
        inquirer.List('choice',
                      message='What operation would you like to perform',
                      choices=['Add keyword', 'Delete keyword', 'Search for keyword', 'Autocomplete by prefix',
                               'Display trie', 'Display trie fast'],
                      carousel=True)
    ]

    choice = inquirer.prompt(question, theme=GreenPassion())['choice']

    if choice != 'Display trie' and choice != 'Display trie fast':
        question2 = [
            inquirer.Text('val',
                          message='Enter a word')
        ]
        val = inquirer.prompt(question2, theme=GreenPassion())['val']
        request(choice, val)
    else:
        request(choice)
