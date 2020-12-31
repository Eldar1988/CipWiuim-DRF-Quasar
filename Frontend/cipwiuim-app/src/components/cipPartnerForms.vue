<template>
  <div class="partner-forms-wrapper q-mt-md">
    <div class="row">
      <div
        v-for="partner in partnerForms"
        :key="partner.id"
        class="col-12 col-sm-4"
        style="padding: 3px"
      >
        <router-link :to="`partner_forms/${partner.slug}`">
          <q-img
            :src="partner.image"
            class="rounded-borders shadow-3 img-overlay-primary"
            height="250px"
          >
            <div class="img-text">
              <p class="text-h6">{{ partner.title }}</p>
            </div>
          </q-img>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "cipPartnerForms",
  computed: {
    partnerForms() {
      return this.$store.getters.getMainData.partnerForms
    }
  }
}
</script>

<style scoped>

</style>
