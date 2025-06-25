import React from "react";
import { useParams, useLocation } from "react-router-dom";
import { useChat } from "../../hooks/useChat";
import "./ChatRoom.scss";
import DeleteIcon from "@mui/icons-material/Delete";

const ChatRoom = () => {
  const { roomName } = useParams();
  const { state } = useLocation();
  const username = state?.username || "Anonymous";

  const {
    messages,
    setMessages,
    message,
    setMessage,
    isLoading,
    error,
    sendChatMessage,
    messagesEndRef,
  } = useChat(roomName, username);

  const handleSubmit = (e) => {
    e.preventDefault();
    sendChatMessage();
  };
  
  const handleDeleteMessage = async (msgID, username, roomName) => {
    if (!window.confirm("Are you sure you want to delete this message?")) {
      return;
    }

    try {
      const response = await fetch(
        `http://localhost:8000/api/rooms/${roomName}/deleteMessage/${msgID}/${username}/`,
        {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      if (!response.ok) {
        throw new Error("Failed to delete message");
      }
    } catch (error) {
      console.error(error);
      alert("❌ An error occurred while deleting the message.");
    }
  };
  
  return (
    <div className="chat-room-container">
      <div className="chat-header">
        <h2>Room: {roomName}</h2>
        <p>Welcome, {username}! </p>
      </div>

      <div className="messages-container">
        {isLoading ? (
          <div className="loading">Loading messages...</div>
        ) : error ? (
          <div className="error">{error}</div>
        ) : (
          messages.map((msg) => (
            <div
              key={msg.id}
              className={`message ${msg.username === username ? "sent" : "received"} ${msg.user_deleted ? "deleted" : ""}`}
            >
              <div className="message-content">
                {msg.username !== username && (
                  <span className="message-sender">{msg.username.toUpperCase()}</span>
                )}
                <p>{msg.content}</p>
                <span className="message-time">
                  {new Date(msg.timestamp).toLocaleString()}
                </span>
              </div>
              {!msg.user_deleted && msg.username === username && (
                <span className="delete-button">
                  <DeleteIcon
                    onClick={() =>
                      handleDeleteMessage(msg.id, msg.username, roomName)
                    }
                  />
                </span>
              )}
            </div>
          ))
        )}
        <div ref={messagesEndRef} />
      </div>

      <form onSubmit={handleSubmit} className="message-form">
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message here..."
          required
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
};

export default ChatRoom;
