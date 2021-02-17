<template>
  <article>
    <q-card
      class="q-pa-md text-center shadow-0"
    >
      <div class="theme-author flex justify-between">
        <p class="text-bold">{{ cardTitle }}</p>
        <q-btn
          label="Профиль"
          unelevated
          outline
          size="sm"
          icon="person"
        />
      </div>
      <q-img :src="profile.avatar" class="q-mt-md" img-class="rounded-borders"/>
      <p class="text-bold q-pt-md">{{ profile.name }}</p>
      <p class="text-grey-8 q-pt-sm">{{ profile.professional }}</p>
    </q-card>
  </article>
</template>

<script>
export default {
  name: "cipProfileCard",
  props: {
    cardTitle: {
      type: String,
      default: ''
    },
    profile: {
      type: Object,
      default: null
    }
  }
}
</script>

<style scoped>

</style>
