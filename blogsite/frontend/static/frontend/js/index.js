var mix = {
    methods: {
        getPosts() {
            this.getData("/api/post/")
                .then(data => {
                    this.posts = data
                }).catch(() => {
                this.posts = []
                console.warn('Ошибка при получении постов')
            })
        },
    },
    mounted() {
        this.getPosts();
    },
    data() {
        return {
            posts: [],
        }
    }
}