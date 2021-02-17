<template>
  <q-card
    dark
    class="bg-gradient-1 my-shadow text-center"
  >
    <q-card-section>
      <p class="text-bold">Автор проекта:</p>
      <q-img :src="company.logo" class="rounded-borders q-mt-md"/>
      <div class="q-mt-md company-card-grid">
        <q-btn
          type="a"
          :href="`tel:${company.phone}`"
          icon="call"
          color="dark"
          unelevated
        />
        <q-btn
          type="a"
          :href="`https://wa.me/${company.whatsapp}`"
          icon="mdi-whatsapp"
          color="dark"
          unelevated
        />
        <q-btn
          :to="`/company/${company.slug}`"
          text-color="dark"
          color="accent"
          label="Профиль"
          unelevated
        />
      </div>

    </q-card-section>
  </q-card>
</template>

<script>
export default {
  name: "cipCompanyCard",
  props: {
    company: {
      type: Object,
      default: null
    }
  }
}
</script>

<style lang="sass">
.company-card-grid
  display: grid
  grid-template-columns: 1fr 1fr 4fr
  grid-gap: 10px
</style>
