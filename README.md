# 💬 ChatWave: Real‑Time Chat Application

A sleek, real‑time chat app built with **Django**, **Django REST Framework**, **Django Channels (WebSockets)**, and **React**.  
Send messages, delete your own messages in real‑time, and chat with friends instantly — no page reload required!

---

## ⚡ Features
- ✅ **Real‑Time Chat:** Messages sent instantly via WebSockets.
- 👥 **User Specific Styling:**  
  - Messages from the current user appear on the **right**.  
  - Messages from other users appear on the **left**.
- 🗑️ **Delete Messages:** Owner can delete messages in real‑time.
- 👥 **Two or More Users Chat Simultaneously:** Enables seamless multi‑user chat.
- 🌐 **Modern Stack:** Django + DRF + Channels + React.
- ⚙️ **Database Support:** SQLite (default), easily extensible.
- 🚀 **Lightweight and Responsive:** Works beautifully across screens.

---

## 🛠️ Tech Stack

| Category       | Technologies                           |
|----------------|----------------------------------------|
| **Backend**    | Python, Django, Django REST Framework  |
| **WebSockets** | Django Channels + Redis                |
| **Database**   | SQLite (default), Redis (for Channels) |
| **Frontend**   | React.js, JavaScript, SCSS, HTML, CSS  |
| **Build Tools**| Node.js, npm                           |
| **Additional** | SCSS for sleek design and layout       |

---

## 🧪 Testing the Application
1. Open **two different browsers** or use **incognito mode** for the second window.
2. Navigate to:
    ```
    http://localhost:3000/
    ```
    or any link shown in the Vite console.
3. Enter a **username** and the **same room name** in both windows.
4. Begin sending messages:
    - ✅ Messages you send appear **on the right**.
    - ✅ Messages from others appear **on the left**.
5. Try deleting one of your messages:
    - 🗑️ It will instantly be replaced by **“This message has been deleted”** across both windows.

---

## ✅ Features Implemented
- 🚀 **Django REST Framework** for REST APIs.
- 🧠 **Django Channels** for real‑time WebSocket connections.
- ⚛️ **React** for a dynamic frontend.
- 🎨 **Modern SCSS** for clean and sleek design.
- 🔄 **Real‑Time Synchronization** across connected clients.
- 🗑️ **Real‑Time Message Deletion** feature.
- 💡 **User‑Specific Messages** with distinct styling.
- 🔥 **Redis** used as a channel layer for scalability.

---

## 👇 How to Clone and Run This Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Aakash-Jha3903/Chat_Application.git
cd backend
```

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Unix/Mac:
source venv/bin/activate
```

```bash
cd backend
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py makemigrations
python manage.py migrate
```

```bash
(optional...)
python manage.py createsuperuser
```

```bash
python manage.py runserver
```

## Note : Redis must be installed and run at 6379 port


```bash
(Now in the another terminal)

cd frontend
```

```bash
npm install
```

```bash
npm run dev
```

### 🚀 Start Chatting
Open the app in **two different browsers** or use **incognito mode**:

- Enter the **same room name** and **different usernames**.
- 💬 Messages will be exchanged **instantly**.
- 🗑️ Owner can **delete messages in real‑time** across both windows.

---

## 👏 Conclusion
This is a robust and modern **Real‑Time Chat Application** using Django and React! It showcases:

- 🚀 **Django, DRF, and Channels** for a fully real‑time experience
- 🧠 **WebSocket consumers** for seamless message handling
- ⚛️ **A sleek React frontend**
- 🎨 **Styled messages** for senders and receivers
- 🔥 **Real‑time delete messages feature**
- ⚡ **Integrated Redis** for efficient, scalability and channel support

---

## 🔮 Future Plans
Here are some ideas and enhancements, I planning for this project:

- 💡 **Typing Indicators** – Show when a user is typing a message.  
- 👥 **Online Status** – Real‑time online/offline status for all connected users.  
- 🔔 **Notifications** – Push notifications for new messages.  
- 🗄️ **Message History Export** – Export chats as `.txt` or `.csv` files.    
- 🔐 **End‑to‑End Encryption** – Enhance privacy and security.  


---


## 🙏🏻 Thank You 
- 👉 Star the repo – It motivates open‑source developers like me.🙂
- 🍴 Fork it – To build and extend your own version.🧑🏻‍💻
- 📢 Share it – So others can benefit too.