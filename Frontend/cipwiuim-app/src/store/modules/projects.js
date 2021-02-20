import axiosInstance from "axios"
import Notify from 'quasar'


export default {
  state: {
    projects: [],
    project: null
  },
  actions: {
    fetchProjects({commit, state}) {
      if (state.projects.length === 0) {
        try{
          return  axiosInstance.get(`${this.getters.getServerURL}/projects/`)
            .then(({data}) => {
              commit('setProjects', data)
            })
        } catch (e) {
          throw e
        }
      }
    },
    fetchProjectDetail({commit}, slug) {
      try {
        return  axiosInstance.get(`${this.getters.getServerURL}/projects/detail/${slug}`)
          .then(({data}) => {
            commit('setProjectDetail', data)
          })
      } catch (e) {
        Notify.create({message: `Не удалось загрузить данные проекта (${e.message}). Пожалуйста, обновите страницу`, position: 'top'})
      }
    }
  },
  mutations: {
    setProjects(state, data) {
      state.projects = data
    },
    setProjectDetail(state, data) {
      state.project = data
    }
  },
  getters: {
    getProjects: (state) => state.projects,
    getProject: (state) => state.project
  }
}
