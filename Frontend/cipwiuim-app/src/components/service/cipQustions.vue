<template>
<div>
  <q-expansion-item
    v-for="item in questions"
    :key="item.question"
    group="questions"
    icon="help"
    :label="item.question"
    header-class="bg-white text-primary rounded-borders"
    class="q-mt-md" expand-icon-class="text-primary"
  >
    <q-card class="q-mt-md rounded-borders">
      <q-card-section>
        {{ item.answer }}
      </q-card-section>
    </q-card>
  </q-expansion-item>
</div>
</template>

<script>
export default {
  name: "cipQustions",
  props: {
    questions: {
      type: Array,
      default: null
    }
  }
}
</script>

<style scoped>

</style>
