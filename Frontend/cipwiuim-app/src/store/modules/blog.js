import axiosInstance from "axios"
import Notify from 'quasar'

export default {
  actions: {
    fetchPosts({commit, state}) {
      if (state.posts.length === 0) {
        return axiosInstance.get(`${this.getters.getServerURL}/blog/`)
          .then(({data}) => {
            commit('setPosts', data)
          })
      }
    },
    fetchFuturePosts({commit, state}) {
      if (state.futurePosts.length === 0) {
        return axiosInstance.get(`${this.getters.getServerURL}/blog/get_future_posts/`)
          .then(({data}) => {
            commit('setFuturePosts', data)
          })
      }
    },
    fetchPost({commit}, slug) {
      try {
        return axiosInstance.get(`${this.getters.getServerURL}/blog/detail/${slug}/`)
        .then(({data}) => {
          commit('setPost', data)
        })
      } catch(e) {
        Notify.create({message: `Не удалось загрузить поста (${e.message}). Пожалуйста, обновите страницу`})
      }
    }

  },
  mutations: {
    setPosts(state, data) {
      state.posts = data
    },
    setFuturePosts(state, data) {
      state.futurePosts = data
    },
    setPost(state, data) {
      state.post = data
    }
  },
  state: {
    post: {},
    posts: [],
    futurePosts: []
  },
  getters: {
    getPosts(state) {
      return state.posts
    },
    getFuturePosts(state) {
      return state.futurePosts
    },
    getPost: (state) => state.post
  }
}
