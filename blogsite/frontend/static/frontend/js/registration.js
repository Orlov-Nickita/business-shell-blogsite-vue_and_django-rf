var mix = {
    methods: {
        registration() {
            this.postData('/api/users/registration/', {
                    username: this.username,
                    last_name: this.last_name,
                    first_name: this.first_name,
                    email: this.email,
                    password: this.password,
                    passwordReply: this.passwordReply
                },
                {
                    headers: {'X-CSRFToken': this.getCookie('csrftoken')}
                })
                .then(() => {
                    alert('Успешная регистрация')
                    location.replace('/')
                })
                .catch(() => {
                    console.warn('Ошибка при регистрации')
                    this.username = ''
                    this.last_name = ''
                    this.first_name = ''
                    this.email = ''
                    this.password = ''
                    this.passwordReply = ''
                })
        },
        getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
    },
    data() {
        return {
            username: null,
            last_name: null,
            first_name: null,
            email: null,
            password: '',
            passwordReply: ''
        }
    }
}