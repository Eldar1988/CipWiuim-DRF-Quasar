import axiosInstance from "axios";
import { Notify } from 'quasar'

export default {
  actions: {
    async fetchMainLayoutData({commit}) {
      try {
        await axiosInstance.get(`${this.getters.getServerURL}`)
          .then(({data}) => {
            commit('setMainLayoutData', data)
          })
      } catch (e) {
        Notify.create({message: `Ошибка соединения (${e.message}). Перезагрузка...`, spinner: true})
        setTimeout(() => {
          location.reload()
        }, 5000)

      }
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
