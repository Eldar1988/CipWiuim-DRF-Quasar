import axiosInstance from "axios";

export default {
  actions: {
    fetchTestimonials({ commit }) {
      return axiosInstance.get(`${this.getters.getServerURL}/testimonials/`)
        .then(({ data }) => {
          commit('setTestimonials', data)
        })
    }
  },
  mutations: {
    setTestimonials(state, data) {
      state.testimonials = data
    }
  },
  state: {
    testimonials: []
  },
  getters: {
    getTestimonials(state) {
      return state.testimonials
    }
  }
}
