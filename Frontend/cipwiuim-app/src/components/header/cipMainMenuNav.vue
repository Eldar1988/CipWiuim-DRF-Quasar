<template>
<nav>
  <q-list separator class="rounded-borders text-dark text-uppercase letter-spacing-5">
<!--    home  -->
    <q-item
      clickable
      to="/"
      exact-active-class="text-primary"
    >
      <q-item-section avatar>
        <q-icon name="mdi-home" />
      </q-item-section>
      <q-item-section>Главная</q-item-section>
    </q-item>
<!--    about   -->
    <q-item
      clickable
      to="/about"
      exact-active-class="text-primary"
    >
      <q-item-section avatar>
        <q-icon name="mdi-charity" />
      </q-item-section>
      <q-item-section>О нас</q-item-section>
    </q-item>
<!--    projects   -->
    <q-expansion-item
      expand-separator
      icon="mdi-finance"
      label="Проекты"
      default-opened
    >
      <q-item
        clickable
        to="/about"
        exact-active-class="text-primary"
      >
        <q-item-section avatar>
          <q-icon name="mdi-arrow-right-bold" />
        </q-item-section>
        <q-item-section>Проект 1</q-item-section>
      </q-item>
    </q-expansion-item>
  </q-list>
</nav>
</template>

<script>
export default {
  name: "cipMainMenuNav"
}
</script>

<style scoped>

</style>
