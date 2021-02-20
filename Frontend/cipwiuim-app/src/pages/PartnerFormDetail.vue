<template>
  <q-page>
    <cip-bread-cumps :current-page-title="partner.title"
                     :pages="[{title: 'Формы партнерства', slug: '/partner_forms'}]"/>
    <cip-page-title :title="partner.title" :subtitle="partner.short_description"/>
    <div class="q-mt-lg bg-white q-pa-md rounded-borders">
      <div v-html="partner.description"></div>
    </div>
    <div class="partner-form-detail-grid section">
      <div>
        <q-card
          class="rounded-borders q-py-lg text-center shadow-0 bg-gradient-1"
          dark
        >
          <q-card-section>
            <p class="text-h6 q-mt-sm">Присоединяйтесь к нам!</p>
            <q-btn
              label="Регистрация"
              icon-right="person_add"
              text-color="primary"
              color="white" unelevated
              class="full-width q-mt-lg  rounded-borders my-shadow q-py-sm"
            />
          </q-card-section>
        </q-card>
        <cip-share style="margin-top: 20px"/>
      </div>

      <div>
        <div class="rounded-borders text-center shadow-0">
          <div>
            <cip-files-list :files="partner.files"/>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import CipPageTitle from "components/cipPageTitle";
import CipBreadCumps from "components/service/cipBreadCumps";
import CipFilesList from "components/service/cipFilesList";
import CipShare from "components/service/cipShare";

export default {
  name: "PartnerFormDetail",
  components: {CipShare, CipFilesList, CipBreadCumps, CipPageTitle},
  computed: {
    partner() {
      return this.$store.getters.getPartnerForm
    }
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('fetchPartnerForm', currentRoute.params.slug)
  }
}
</script>

<style lang="sass">

.partner-form-detail-grid
  display: grid
  grid-gap: 20px
  grid-template-columns: 1fr 2fr

@media screen and (max-width: 800px)
  .partner-form-detail-grid
    grid-template-columns: 1fr
    grid-gap: 50px


</style>
