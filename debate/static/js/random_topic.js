document.getElementById('topicButton').onclick = function() {
    fetch('/random-topic/', {
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const topicDisplay = document.getElementById('topicDisplay');
        topicDisplay.innerText = data.topic;
        topicDisplay.style.opacity = 0;
        setTimeout(() => {
            topicDisplay.style.opacity = 1;
        }, 10); // Timeout to trigger CSS transition
    })
    .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
    });
};

