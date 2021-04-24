import axios from 'axios'

export default {
  state: {
    points: []
  },
  actions: {
    async loadMapPoints({commit}, region, pointType='None') {
      return axios.get(`${this.getters.getServerURL}/map/points/${region}/${pointType}/`)
        .then(({data}) => commit('setPoints', data))
    }
  },
  mutations: {
    setPoints(state, data) {
      state.points = data
    }
  },
  getters: {
    getPoints: state => state.points
  }
}
