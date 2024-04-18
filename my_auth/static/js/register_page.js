function registerUser() {
    var formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value,
        role: document.getElementById('role').value
    };

    // Проверка почты
    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(formData.email)) {
        alert("Введите корректный адрес электронной почты.");
        return;
    }

    // Проверка роли
    if (formData.role !== "Линкольн" && formData.role !== "Дуглас" && formData.role !== "Lincoln" && formData.role !== "Duoglas") {
        alert("Роль должна быть либо 'Линкольн', либо 'Дуглас'.");
        return;
    }

    fetch('http://localhost:8000/api/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
    
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            // Проверяем, содержит ли ответ сообщение об ошибке о занятой почте или никнейме
            alert(data.error); // Отображаем сообщение об ошибке
        } else {
            console.log('Success:', data);
            alert("Регистрация прошла успешно!");
            window.location.href = '/login/'; // Redirect to login page
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        alert("Ошибка регистрации.");
    });
}