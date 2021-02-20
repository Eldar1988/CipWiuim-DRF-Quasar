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
    },
    async fetchAboutInfo({commit, state}) {
      if (!state.company) {
        try {
          await axiosInstance.get(`${this.getters.getServerURL}/about/`)
            .then(({data}) => {
              commit('setCompanyInfo', data)
            })
        } catch (e) {
          throw e
        }
      }
    },
    async fetchRules({commit, state}) {
      if (!state.rules) {
        try {
          await axiosInstance.get(`${this.getters.getServerURL}/rules/`)
            .then(({data}) => {
              commit('setRules', data)
            })
        } catch (e) {
          throw e
        }
      }
    },
    async fetchQuestions({commit, state}) {
      if (!state.questions) {
        try {
          await axiosInstance.get(`${this.getters.getServerURL}/questions/`)
            .then(({data}) => {
              commit('setQuestions', data)
            })
        } catch (e) {
          throw e
        }
      }
    }
  },
  mutations: {
    setMainLayoutData(state, data) {
      state.mainData = data
    },
    setCompanyInfo(state, data) {
      state.company = data
    },
    setRules(state, data) {
      state.rules = data
    },
    setQuestions(state, data) {
      state.questions = data
    }
   },
  state: {
    mainData: [],
    company: null,
    rules: null,
    questions: null
  },
  getters: {
    getMainData: (state) => state.mainData,
    getCompanyInfo: (state) => state.company,
    getRules: (state) => state.rules,
    getQuestions: (state) => state.questions
  }
}
