css = '''
<style>
    .chat-message {
        padding: 1.5rem;
        border-radius: 1rem;
        margin-bottom: 1rem;
        display: flex;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    .chat-message.user {
        background-color: #2b313e;
    }

    .chat-message.bot {
        background-color: #475063;
    }

    .chat-message .avatar {
        width: 20%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .chat-message .avatar img {
        max-width: 100%;
        max-height: 100%;
        border-radius: 50%;
        object-fit: cover;
        transition: transform 0.3s ease;
    }

    .chat-message .message {
        width: 80%;
        padding: 1.5rem;
        color: #fff;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .chat-message:hover {
        transform: scale(1.02);
        transition: transform 0.3s ease;
    }
</style>
'''

bot_template = '''
<div class="chat-message bot" onmouseover="hoverEffect(this)" onmouseout="removeHoverEffect(this)">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>

'''

user_template = '''
<div class="chat-message user" onmouseover="hoverEffect(this)" onmouseout="removeHoverEffect(this)">
    <div class="avatar">
        <img src="https://i.ibb.co/fnyCccz/images.png"alt="User Avatar">
    </div>    
    <div class="message">{{MSG}}</div>
</div>



'''
