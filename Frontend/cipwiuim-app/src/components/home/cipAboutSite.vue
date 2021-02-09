<template>
  <section class="section">
    <div class="about-site-wrapper">
      <div class="heading text-center">
        <p class="light-text">Cip Wiuim</p>
        <h3 class="section-title">
          На нашем сайте вы найдете
        </h3>
      </div>
      <div class="about-site-gid">
        <div
          v-for="content in cardsContent"
          :key="content.title"
          class=""
        >
          <q-card
            class="q-pa-md text-center shadow-0"
            style="min-height: 100%"
          >
            <q-btn
              :icon="content.icon"
              size="lg"
              class="bg-gradient-1 my-shadow"
              text-color="white"
              round unelevated
            />
            <h4 class="text-h6 q-mt-lg">
              {{ content.title }}
            </h4>
            <p class="q-mt-md">
              {{ content.text }}
            </p>
            <q-btn
              label="Подробнее"
              outline
              color="primary"
              class="q-mt-md q-px-md"
              size="md"
              :to="content.link"
            />
          </q-card>
        </div>
      </div>
    </div>

  </section>
</template>

<script>
export default {
  name: "cipAboutSite",
  data() {
    return {
      cardsContent: [
        {icon: 'mdi-finance', title: 'Проекты', link: '/projects', text: '«CIP WIUIM» открывает новые горизонты для жителей Центрально-азиатского региона. Теперь у всех есть возможность стать инвестором в размещаемых проектах. Принимайте активное участие в размещении своих вкладов и получайте гарантированный стабильный доход!'},
        {icon: 'mdi-forum-outline', title: 'Форум', link: '/forum', text: 'С нами вы узнаете: что такое дуальное образование и чем оно лучше традиционного, основу экономики Миниполиса «Евро Таун», принципы работы Национальной ассоциации застройщиков, для чего нужна Национальная конная академия, что такое социально-частное партнерство и многое другое.'},
        {icon: 'mdi-newspaper-variant-multiple', title: 'Информационный блог', link: '/blog', text: 'Где бы человек не находился, он там и должен улучшить свое благосостояние. Вместе с «CIP WIUIM» вы сможете его улучшить не только для себя, но и для всех жителей Центрально-азиатского региона. Не пропустите последние новости, присоединяйтесь к нашему блогу!'},
        {icon: 'mdi-map-search-outline', title: 'Виды деятельности на карте', link: '/activities', text: 'Представляем вашему вниманию развернутую структуру всех населенных пунктов Республики Казахстан. На нашей карте вы сможете ознакомится со всеми объектами населенных пунктов, такими как: улицы, жилые дома, акиматы, школы, детские сады, промышленные производства, торговые точки, больницы, аптеки, ЦОМы и так далее.'},
      ]
    }
  },
}
</script>

<style lang="sass">
.about-site-gid
  margin-top: 30px
  display: grid
  grid-template-columns: 1fr 1fr
  @media screen and (max-width: 650px)
    grid-template-columns: 1fr
  grid-gap: 10px

</style>
