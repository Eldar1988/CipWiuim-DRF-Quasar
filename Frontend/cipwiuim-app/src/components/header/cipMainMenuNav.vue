<template>
  <nav>
    <!--    Menu   -->
    <q-list separator class="rounded-borders text-dark text-uppercase letter-spacing-5 text-weight-bold">
      <!--    home  -->
      <q-item
        clickable
        to="/"
        exact-active-class="text-primary"
      >
        <q-item-section avatar>
          <q-icon name="mdi-home"/>
        </q-item-section>
        <q-item-section>Главная</q-item-section>
      </q-item>
      <!--    partner forms   -->
      <q-item
        clickable
        to="/partner_forms"
        exact-active-class="text-primary"
      >
        <q-item-section avatar>
          <q-icon name="mdi-charity"/>
        </q-item-section>
        <q-item-section>Формы партнерства</q-item-section>
      </q-item>
      <!--    projects   -->
      <q-expansion-item
        expand-separator
        icon="mdi-finance"
        label="Проекты"
      >
        <q-item
          clickable
          to="/projects"
          exact-active-class="text-primary"
          class="q-ml-sm text-weight-regular"
          style="text-transform: none"
        >
          <q-item-section avatar>
            <q-icon name="mdi-arrow-right-bold"/>
          </q-item-section>
          <q-item-section>Все проекты</q-item-section>
        </q-item>
        <q-item
          v-for="project in projects"
          :key="project.id"
          clickable
          :to="`/projects/${project.slug}`"
          exact-active-class="text-primary"
          class="q-ml-sm text-weight-regular"
          style="text-transform: none"
        >
          <q-item-section avatar>
            <q-icon name="mdi-arrow-right-bold"/>
          </q-item-section>
          <q-item-section>{{ project.title }}</q-item-section>
        </q-item>
      </q-expansion-item>
      <!--    blog   -->
      <q-expansion-item
        expand-separator
        icon="mdi-newspaper-variant-multiple"
        label="Блог"
      >
        <q-item
          v-for="category in postCategories"
          :key="category.id"
          clickable
          :to="`/blog/${category.slug}`"
          exact-active-class="text-primary"
          class="q-ml-sm text-weight-regular"
          style="text-transform: none"
        >
          <q-item-section avatar>
            <q-icon name="mdi-arrow-right-bold"/>
          </q-item-section>
          <q-item-section>{{ category.title }}</q-item-section>
        </q-item>
      </q-expansion-item>
      <!--    forum   -->
      <q-expansion-item
        expand-separator
        icon="mdi-forum-outline"
        label="Форум"
      >
        <q-item
          clickable
          to="/forum"
          exact-active-class="text-primary"
          class="q-ml-sm text-weight-regular"
          style="text-transform: none"
        >
          <q-item-section avatar>
            <q-icon name="mdi-arrow-right-bold"/>
          </q-item-section>
          <q-item-section>Все темы форума</q-item-section>
        </q-item>
        <q-item
          v-for="theme in forumThemes"
          :key="theme.id"
          clickable
          :to="`/forum/${theme.slug}`"
          exact-active-class="text-primary"
          class="q-ml-sm text-weight-regular"
          style="text-transform: none"
        >
          <q-item-section avatar>
            <q-icon name="mdi-arrow-right-bold"/>
          </q-item-section>
          <q-item-section>{{ theme.title }}</q-item-section>
        </q-item>
      </q-expansion-item>
      <!--      about   -->
      <q-item
        clickable
        to="/about"
        exact-active-class="text-primary"
      >
        <q-item-section avatar>
          <q-icon name="mdi-lightbulb-on-outline"/>
        </q-item-section>
        <q-item-section>О нас</q-item-section>
      </q-item>
      <!--    activities   -->
      <q-item
        clickable
        to="/activities"
        exact-active-class="text-primary"
      >
        <q-item-section avatar>
          <q-icon name="mdi-map-search-outline"/>
        </q-item-section>
        <q-item-section>Виды деятельности</q-item-section>
      </q-item>
      <!--    site rules   -->
      <q-item
        clickable
        to="/rules"
        exact-active-class="text-primary"
      >
        <q-item-section avatar>
          <q-icon name="mdi-playlist-check"/>
        </q-item-section>
        <q-item-section>Правила сайта</q-item-section>
      </q-item>
      <!--    questions   -->
      <q-item
        clickable
        to="/questions"
        exact-active-class="text-primary"
      >
        <q-item-section avatar>
          <q-icon name="mdi-comment-question-outline"/>
        </q-item-section>
        <q-item-section>Вопросы и ответы</q-item-section>
      </q-item>
      <!--    contacts   -->
      <q-item
        clickable
        to="/contacts"
        exact-active-class="text-primary"
      >
        <q-item-section avatar>
          <q-icon name="mdi-google-maps"/>
        </q-item-section>
        <q-item-section>Контакты</q-item-section>
      </q-item>
    </q-list>
    <!--    ===================   -->
    <!--    Partner Banners   -->
    <q-list class="q-mt-md">
      <!--    partner forms   -->
      <q-item
        v-for="partner in partnerForms"
        :key="partner.id"
        clickable
        :to="`/partner_forms/${partner.slug}`"
      >
        <q-item-section>
          <q-img :src="partner.banner" height="150px" class="rounded-borders img-overlay">
            <template v-slot:loading>
              <q-skeleton class="full-width" height="150px" />
            </template>
            <div class="img-text">
              <span class="text-h6">{{ partner.banner_title }}</span>
            </div>
          </q-img>
        </q-item-section>
      </q-item>
    </q-list>
    <!--    ===================   -->
  </nav>
</template>

<script>
export default {
  name: "cipMainMenuNav",
  computed: {
    projects() {
      return this.$store.getters.getMainData.projects
    },
    postCategories() {
      return this.$store.getters.getMainData.postCategories
    },
    forumThemes() {
      return this.$store.getters.getMainData.forumThemes
    },
    partnerForms() {
      return this.$store.getters.getMainData.partnerForms
    },
  }
}
</script>

<style lang="sass">

</style>
