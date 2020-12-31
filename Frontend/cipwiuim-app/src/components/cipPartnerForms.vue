<template>
  <div class="partner-forms-wrapper">
    <div class="row">
      <div
        v-for="partner in partnerForms"
        :key="partner.id"
        class="col-12 col-sm-4 q-mt-md"
        style="padding: 3px"
      >
        <router-link :to="`partner_forms/${partner.slug}`">
          <article>
            <q-img
              :src="partner.image"
              class="rounded-borders shadow-3 img-overlay-primary"
              height="250px"
            >
              <div class="img-text">
                <p class="text-h6">{{ partner.title }}</p>
                <p class="ellipsis-2-lines">{{ partner.short_description }}</p>
              </div>
            </q-img>
          </article>
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
