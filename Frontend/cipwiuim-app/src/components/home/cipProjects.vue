<template>
  <section class="section">
    <div class="projects-wrapper">
      <div class="heading text-center">
        <h3 class="section-title">
          Проекты
        </h3>
        <p class="q-mt-md">CIP WIUIM<br>Мы открывает новые горизонты для жителей Центрально-азиатского региона.
          <br>Теперь у всех есть возможность стать инвестором в размещаемых проектах.
          <br>Принимайте активное участие в размещении своих вкладов и получайте гарантированный стабильный доход!</p>
      </div>
      <cip-projects-list-scroll-x />
    </div>
  </section>
</template>

<script>
import CipProjectsListScrollX from "components/projects/cipProjectsListScrollX";
export default {
name: "cipProjects",
  components: {CipProjectsListScrollX}
}
</script>

<style scoped>

</style>
