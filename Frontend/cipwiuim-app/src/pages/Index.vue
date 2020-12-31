<template>
  <q-page>
    <cip-home-slider />
    <cip-partner-forms />
    <cip-about-site />
  </q-page>
</template>

<script>
import CipHomeSlider from "components/home/cipHomeSlider";
import CipPartnerForms from "components/cipPartnerForms";
import CipAboutSite from "components/home/cipAboutSite";
export default {
  name: 'PageIndex',
  components: {CipAboutSite, CipPartnerForms, CipHomeSlider}
}
</script>
