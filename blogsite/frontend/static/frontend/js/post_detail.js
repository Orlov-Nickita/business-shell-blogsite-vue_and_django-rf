var mix = {
    methods: {
        getPostDetail() {
            const post_id = location.pathname.replace('/post/', '').replace('/', '')
            this.getData(`/api/post/${post_id}`)
                .then(data => {
                    this.post = data[0]
                }).catch(() => {
                this.post = []
                console.warn('Ошибка при получении поста')
            })
        },
        postComment() {
            const post_id = location.pathname.replace('/post/', '').replace('/', '')
            this.postData('/api/comment/create/', {
                    comment: this.comment,
                    post: post_id
                },
                {
                    headers: {'X-CSRFToken': this.getCookie('csrftoken')}
                })
                .then(() => {
                    location.replace(`/post/${post_id}`)
                })
                .catch(() => {
                    console.warn('Ошибка при создании поста')
                    this.comment = ''
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

    mounted() {
        this.getPostDetail();
    },
    data() {
        return {
            post: {
                author: {
                    first_name: '',
                    last_name: '',
                    username: ''
                },
            },
            comment: ''
        }
    }
}