import axios from 'axios'

export default {
  state: {
    points: [],
    region: {},
    point: {}
  },
  actions: {
    async loadMapPoints({commit}, region, pointType='None') {
      return axios.get(`${this.getters.getServerURL}/map/points/${region}/${pointType}/`)
        .then(({data}) => commit('setPoints', data))
    },
    async loadMapPoint({commit}, slug) {
      return axios.get(`${this.getters.getServerURL}/map/point/${slug}/`)
        .then(({data}) => commit('setPoint', data))
    }
  },
  mutations: {
    setPoints(state, data) {
      state.points = data.points
      state.region = data.region
    },
    setPoint(state, data) {
      state.point = data
    },
  },
  getters: {
    getPoints: state => state.points,
    getPoint: state => state.point,
    getRegion: state => state.region
  }
}
