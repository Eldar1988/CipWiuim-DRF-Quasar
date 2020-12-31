import axiosInstance from "axios";

export default {
  actions: {
    fetchMainLayoutData({commit}) {
      return axiosInstance.get(`${this.getters.getServerURL}`)
        .then(({data}) => {
          commit('setMainLayoutData', data)
        })
    }
  },
  mutations: {
    setMainLayoutData(state, data) {
      state.mainData = data
    }
  },
  state: {
    mainData: []
  },
  getters: {
    getMainData(state) {
      return state.mainData
    }
  }
}
