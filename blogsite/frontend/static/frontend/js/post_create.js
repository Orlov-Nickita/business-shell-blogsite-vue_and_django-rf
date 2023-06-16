var mix = {
    methods: {
        post_create() {
            this.postData('/api/post/create/', {
                    post_title: this.post_title,
                    post_description: this.post_description,
                },
                {
                    headers: {'X-CSRFToken': this.getCookie('csrftoken')}
                })
                .then(() => {
                    alert('Успешно добавлен новый пост')
                    location.replace('/')
                })
                .catch(() => {
                    console.warn('Ошибка при создании поста')
                    this.post_title = ''
                    this.post_description = ''
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
            post_title: null,
            post_description: null,
        }
    }
}