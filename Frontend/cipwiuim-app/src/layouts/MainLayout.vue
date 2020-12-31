<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class="bg-primary text-white header">
      <q-toolbar>
        <!--        Logo   -->
        <cip-logo/>
        <!--        =============   -->
        <q-space/>
        <!--        Consult button   -->
        <cip-consultation/>
        <!--        ==============   -->
        <!--        Account button   -->
        <q-btn dense outline round icon="mdi-account-tie" class="hide-on-mobile q-mr-lg"/>
        <!--        ==============   -->
        <!--        Menu button   -->
        <q-btn dense flat size="lg" round icon="mdi-menu" @click="right = !right"/>
        <!--        ==============   -->
      </q-toolbar>
    </q-header>

    <!--    Drawer menu   -->
    <q-drawer show-if-above v-model="right" side="right" bordered>
      <!-- drawer content -->
      <!--      Mobile menu toolbar   -->
      <q-toolbar class="bg-primary hide-on-desktop mobile-flex" style="height: 60px">
        <q-toolbar-title class="text-white text-uppercase">
          <div class="q-px-sm flex" style="align-items: center">
            Меню
            <q-space/>
            <q-btn
              icon="mdi-close"
              flat
              padding="0"
              @click="right=false"
            />
          </div>
        </q-toolbar-title>
      </q-toolbar>
      <!--      Consultation mobile   -->
      <cip-consultation color="primary" :hideOnMobile="false"/>
      <!--      Main menu   -->
      <cip-main-menu-nav/>
    </q-drawer>
    <!--    ===============   -->

    <q-page-container class="page-container">
      <router-view/>
    </q-page-container>

  </q-layout>
</template>

<script>
import CipLogo from "components/header/cipLogo";
import CipConsultation from "components/header/cipConsultation";
import CipMainMenuNav from "components/header/cipMainMenuNav";

export default {
  components: {CipMainMenuNav, CipConsultation, CipLogo},
  data() {
    return {
      right: false
    }
  },
  mounted() {
  },
  preFetch({ store }) {
    return store.dispatch('fetchMainLayoutData')
  }
}
</script>

<style lang="sass">
.header
  background: linear-gradient(145deg, #1976d2 11%, #003399 75%) !important

.page-container
  max-width: 98%
  margin: 15px auto 0

@media screen and (max-width: 650px)
  .page-container
    margin: 5px auto 0
</style>
