const {createApp} = Vue

createApp({
    delimiters: ['${', '}$'],
    mixins: [window.mix ? window.mix : {}],
    methods: {
        postData(url, payload, config) {
            return axios.post(url, payload, config ? config : {})
                .then(response => {
                    return response.data ? response.data : response.json?.()
                }).catch((data) => {
                    alert(data.response.request.responseText)
                    console.warn('Метод ' + url + ' не реализован')
                    throw new Error('no "post" method')
                })
        },
        getData(url, payload) {
            return axios.get(url, {params: payload})
                .then(response => {
                    return response.data ? response.data : response.json?.()
                })
                .catch(() => {
                    console.warn('Метод ' + url + ' не реализован')
                    throw new Error('no "get" method')
                })
        },

    },

}).mount('#site')