import Vue from 'vue'
import Vuex from 'vuex'
import axiosInstance from 'axios'

// import example from './module-example'

Vue.use(Vuex)

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

export default function (/* { ssrContext } */) {
  const Store = new Vuex.Store({

    state: () => ({
      serverURL: 'http://192.168.0.199:8000',
      mainData: []
    }),

    mutations: {
      setMainLayoutData(state, data) {
        state.mainData = data
      }
    },

    actions: {
      fetchMainLayoutData({ commit }) {
        return axiosInstance.get(`${this.getters.getServerURL}`)
          .then(({ data }) => {
            commit('setMainLayoutData', data)
          })
      }
    },

    getters: {
      getServerURL(state) {
        return state.serverURL
      },
      getMainData(state) {
        return state.mainData
      }
    },

    // enable strict mode (adds overhead!)
    // for dev mode only
    strict: process.env.DEBUGGING
  })

  return Store
}
