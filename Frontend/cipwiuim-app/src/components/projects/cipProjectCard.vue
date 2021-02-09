<template>
<div>
  <q-card class="my-card shadow-0">
    <q-img :src="project.image" height="230px">
      <template v-slot:loading>
        <q-skeleton class="full-width" height="230px" />
      </template>
    </q-img>
    <q-card-section>

      <div class="row no-wrap items-center">
        <div class="col text-h6 ellipsis">
          <router-link :to="`/projects/${project.slug}`">
          {{ project.title }}
          </router-link>
          <q-tooltip>
            {{ project.title }}
          </q-tooltip>
        </div>
      </div>
    </q-card-section>

    <q-card-section class="q-pt-none">
      <div class="text-grey ellipsis-3-lines">
        {{ project.description }}
      </div>
      <q-btn
        color="primary" unelevated
        class="full-width bg-gradient-1 q-mt-md blue-shadow"
        icon-right="mdi-chevron-right"
        :to="`/projects/${project.slug}`"
      >
        Подробнее
        <q-tooltip>
          Перейти к проекту
        </q-tooltip>
      </q-btn>
    </q-card-section>


  </q-card>
</div>
</template>

<script>
export default {
  name: "cipProjectCard",
  props: {
    project: {
      type: Object,
      default: null
    }
  }
}
</script>

<style scoped>

</style>
