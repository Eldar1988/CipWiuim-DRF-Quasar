import axiosInstance from "axios";

export default {
  actions: {
    fetchPosts({ commit }) {
      return axiosInstance.get(`${this.getters.getServerURL}/blog/`)
        .then(({ data }) => {
          commit('setPosts', data)
        })
    }
  },
  mutations: {
    setPosts(state, data) {
      state.posts = data
    }
  },
  state: {
    posts: []
  },
  getters: {
    getPosts(state) {
      return state.posts
    }
  }
}
