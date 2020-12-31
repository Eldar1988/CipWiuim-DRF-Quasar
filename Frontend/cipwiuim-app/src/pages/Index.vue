<template>
  <q-page>
    <cip-home-slider />
    <cip-partner-forms />
    <cip-about-site />
    <cip-projects/>
  </q-page>
</template>

<script>
import CipHomeSlider from "components/home/cipHomeSlider";
import CipPartnerForms from "components/cipPartnerForms";
import CipAboutSite from "components/home/cipAboutSite";
import CipProjects from "components/home/cipProjects";
export default {
  name: 'PageIndex',
  components: {CipProjects, CipAboutSite, CipPartnerForms, CipHomeSlider}
}
</script>
