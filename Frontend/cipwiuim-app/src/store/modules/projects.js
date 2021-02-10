import axiosInstance from "axios";

export default {
  state: {
    projects: [],
    project: null
  },
  actions: {
    fetchProjects({commit}) {
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
  mutations: {
    setProjects(state, data) {
      state.projects = data
    }
  },
  getters: {
    getProjects: (state) => state.projects,
    getProject: (state) => state.project
  }
}
