import AxiosInstance from 'axios'
import Notify from 'quasar'
import axiosInstance from "axios";

export default {
  state: {
    themes: [],
    theme: {}
  },
  actions: {
    fetchForumThemes({commit}) {
      try {
        return AxiosInstance.get(`${this.getters.getServerURL}/forum/`)
          .then(({data}) => commit('setForumThemes', data))
      } catch (e) {
        Notify.create({message: `Не удалось загрузить темы форума (${e.message})`, position: 'top'})
      }
    },
    fetchForumThemeData({commit}, slug) {
      try {
        return axiosInstance.get(`${this.getters.getServerURL}/forum/detail/${slug}`)
          .then(({data}) => {
            commit('setForumTheme', data)
          })
      } catch (e) {
        Notify.create({message: `Не удалось загрузить тему форума (${e.message})`, position: 'top'})
      }
    }
  },
  mutations: {
    setForumThemes(state, data) {
      state.themes = data
    },
    setForumTheme(state, data) {
      state.theme = data
    }
  },
  getters: {
    getForumThemes: (state) => state.themes,
    getForumTheme: (state) => state.theme
  }
}
