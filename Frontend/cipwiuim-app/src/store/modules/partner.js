import axiosInstance from "axios";

export default {
  state: {
    partnerForm: {}
  },
  actions: {
    fetchPartnerForm({commit, state}, slug) {
      try {
        return axiosInstance.get(`${this.getters.getServerURL}/partner_forms/${slug}/`)
          .then(({data}) => {
            commit('setPartnerForm', data)
          })
      } catch (e) {
        throw e
      }
    }
  },
  mutations: {
    setPartnerForm(state, data) {
      state.partnerForm = data
    }
  },
  getters: {
    getPartnerForm: (state) => state.partnerForm
  }
}
