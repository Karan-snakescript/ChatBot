

function appendMessage(content, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message ' + sender;
    messageDiv.innerText = content;
    document.getElementById('chatMessages').appendChild(messageDiv);
    document.getElementById('chatMessages').scrollTop = document.getElementById('chatMessages').scrollHeight;
}

function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    if (userInput.trim() === '') return;

    appendMessage(userInput, 'user');
    document.getElementById('userInput').value = '';

    $.ajax({
        type: 'POST',
        url: '{% url "chatbot" %}',
        data: {
            'message': userInput,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function(response) {
            appendMessage(response.message, 'bot');
        },
        error: function(){
            alert('Error occurred while communicating with the server.');
        }
    });
}