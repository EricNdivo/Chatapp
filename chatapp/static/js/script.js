const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');
const chatMessages = document.getElementById('chat-messages');


let ws;

// Function to add a new message to the chat window
function addMessage(message) {
  const messageElement = document.createElement('div');
  messageElement.classList.add('message');
  messageElement.textContent = message;
  chatMessages.appendChild(messageElement);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Event listener for the send button click
sendButton.addEventListener('click', () => {
  const message = messageInput.value.trim();
  if (message !== '') {
    addMessage(`You: ${message}`);
    // Send the message to the server or handle it as needed
    messageInput.value = '';
  }
});

// Event listener for the Enter key press in the message input
messageInput.addEventListener('keypress', (event) => {
  if (event.key === 'Enter') {
    sendButton.click();
    event.preventDefault();
  }
});

function init() {
    if (ws) {
        ws.onerror = ws.onopen = ws.onclose =null;
        ws.onclose();
    }

    ws = new WebSocket('ws//localhost:8080');
    ws.onopen = () => {

        console.log('Connection Opened!');
        //let username=prompt("Please enter your name:");
    }

    ws.onmessage = ({ data }) => showMessage(data);
    ws.onclose = function() {
        ws = null;
    }

    sendButton.onclick = function() {
        if (!ws) {
            showMessage('No WebSocket connection :');
            return ;
        }

        ws.send(messageBox.value);
        showMessage(messageBox.value);
    }
    init();
    }