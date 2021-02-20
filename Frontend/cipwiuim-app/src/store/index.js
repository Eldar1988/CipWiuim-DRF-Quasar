import Vue from 'vue'
import Vuex from 'vuex'
import main from './modules/main'
import blog from './modules/blog'
import projects from './modules/projects'
import forum from './modules/forum'
import partner from './modules/partner'

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
      // serverURL: 'http://192.168.0.199:8000',
      serverURL: 'https://api.cipwiuim.com',
      // serverURL: 'http://0.0.0.0:8000',
    }),

    mutations: {
    },

    actions: {
    },

    getters: {
      getServerURL(state) {
        return state.serverURL
      }
    },
    modules: {
      main,
      blog,
      projects,
      forum,
      partner
    },

    // enable strict mode (adds overhead!)
    // for dev mode only
    strict: process.env.DEBUGGING
  })

  return Store
}
