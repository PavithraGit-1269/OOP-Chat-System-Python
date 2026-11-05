class User:
    def __init__(self, username):
        self.username = username

class Message:
    def __init__(self, sender, content):
        self.sender = sender  
        self.content = content  
        
    def __str__(self):
        return f"{self.sender.username}: {self.content}"

class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.active_users = []  
        self.chat_history = []  

    def join_room(self, user):
        if user not in self.active_users:
            self.active_users.append(user)
            print(f"[SYSTEM] {user.username} has joined '{self.room_name}'.")

    def leave_room(self, user):
        if user in self.active_users:
            self.active_users.remove(user)
            print(f"[SYSTEM] {user.username} has left '{self.room_name}'.")

    def send_message(self, user, content):
        if user in self.active_users:
            new_msg = Message(user, content)
            self.chat_history.append(new_msg)
        else:
            print(f"[ERROR] {user.username} must join the room to send messages.")

    def view_history(self):
        print(f"\n--- Chat History for '{self.room_name}' ---")
        if not self.chat_history:
            print("(No messages yet)")
        else:
            for msg in self.chat_history:
                print(msg)
        print("-" * 35)


# --- Execution and Testing ---

# 1. Create a chatroom and some users
dev_room = ChatRoom("Python Developers")
user1 = User("Alice")
user2 = User("Bob")

# 2. Users join the room
dev_room.join_room(user1)
dev_room.join_room(user2)
print()

# 3. Sending messages back and forth
dev_room.send_message(user1, "Hey Bob! Are you working on Q10?")
dev_room.send_message(user2, "Yeah! Just finishing up the ChatRoom class layout.")
dev_room.send_message(user1, "Awesome, let me know if it runs successfully.")
print()

# 4. A user leaves the room
dev_room.leave_room(user1)

# 5. Trying to send a message after leaving (Should show an error)
dev_room.send_message(user1, "Wait, I forgot to ask one more thing!")

# 6. View the final history of the room
dev_room.view_history()
