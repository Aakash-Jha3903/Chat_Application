import { useState, useCallback, useRef, useEffect } from "react";
import useWebSocket from "react-use-websocket";

export const useChat = (roomName, username) => {
  const [messages, setMessages] = useState([]);
  const [message, setMessage] = useState("");
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const messagesEndRef = useRef(null);

  const { sendMessage, lastMessage } = useWebSocket(
    `ws://localhost:8000/ws/chat/${roomName}/`,
    {
      shouldReconnect: () => true,
      reconnectAttempts: 10,
      reconnectInterval: 3000,
    }
  );

  // ✅ Initial load
  useEffect(() => {
    const fetchMessages = async () => {
      try {
        const response = await fetch(`http://localhost:8000/api/rooms/${roomName}/messages/`);
        const data = await response.json();
        setMessages(data);
        setIsLoading(false);
      } catch (err) {
        setError("Failed to load messages");
        setIsLoading(false);
      }
    };
    fetchMessages();
  }, [roomName]);

  // ✅ WebSocket listener
  useEffect(() => {
    if (!lastMessage) return;

    const data = JSON.parse(lastMessage.data);

    if (data.type === "chat.message_deleted") {
      setMessages((prev) =>
        prev.map((m) =>
          m.id === data.msg_id
            ? {
                ...m,
                user_deleted: true,
                content: "This message has been deleted",
              }
            : m
        )
      );
    } else if (data.type === "chat.message") {
      setMessages((prev) => [...prev, data]);
    }
  }, [lastMessage]);

  // ✅ Auto scroll
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  // ✅ Sending a new message
  const sendChatMessage = useCallback(() => {
    if (message.trim()) {
      sendMessage(
        JSON.stringify({
          message,
          username,
          room_name: roomName,
        })
      );
      setMessage("");
    }
  }, [message, username, roomName, sendMessage]);

  return {
    messages,
    message,
    setMessage,
    isLoading,
    error,
    sendChatMessage,
    messagesEndRef,
    setMessages,
  };
};
