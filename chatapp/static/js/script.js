const socket = io();

socket.on("message", (data) => {
  const messages = document.querySelector(".messages");
  const message = document.createElement("div");
  message.innerHTML = data.message;
  messages.appendChild(message);
});

document.querySelector("form").addEventListener("submit", (event) => {
  event.preventDefault();
  const message = document.querySelector("input[name=message]").value;
  socket.emit("message", { message });
});
