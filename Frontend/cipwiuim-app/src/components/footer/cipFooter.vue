<template>
  <section>
    <footer class="footer q-py-xl bg-gradient-1 text-white rounded-borders">
      <div class="footer-grid">
        <div class="footer-menu text-left">
          <ul>
            <li>
              <router-link to="/" class="text-white">
                <q-icon name="chevron_right" color="white"/>
                Главная
              </router-link>
            </li>
            <li>
              <router-link to="/partner_forms" class="text-white">
                <q-icon name="chevron_right" color="white"/>
                Формы партнерства
              </router-link>
            </li>
            <li>
              <router-link to="/projects" class="text-white">
                <q-icon name="chevron_right" color="white"/>
                Проекты
              </router-link>
            </li>
            <li>
              <router-link to="/blog" class="text-white">
                <q-icon name="chevron_right" color="white"/>
                Блог
              </router-link>
            </li>
            <li>
              <router-link to="/forum" class="text-white">
                <q-icon name="chevron_right" color="white"/>
                Форум
              </router-link>
            </li>

          </ul>
        </div>
        <div class="footer-contacts text-left ">
          <p><q-icon name="room"/> {{ contacts.address }}</p>
          <a :href="`tel:{contacts.phone}`" class="block text-white"><q-icon name="call"/> {{ contacts.phone }}</a>
          <a :href="`https://wa.me/${contacts.whatsapp}`" class="block text-white"><q-icon name="mdi-whatsapp"/> {{ contacts.whatsapp }}</a>
          <a :href="`mailto:${contacts.email}`" class="block text-white"><q-icon name="alternate_email"/> {{ contacts.email }}</a>
          <div class="">
            <div class="flex q-mt-sm">
              <div
                v-for="i in socials"
                :key="i.id"
              >
                <q-btn
                  :icon="i.icon"
                  color="white"
                  round unelevated flat dense
                  class="q-mr-md"
                  type="a"
                  :href="i.url"
                  target="_blank"
                />
              </div>
            </div>
          </div>
        </div>
        <div>
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2903.508725349658!2d76.95652931571827!3d43.30360888298341!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x38836db517f8d783%3A0x951c31c0e3416169!2sCIP%20WIUIM!5e0!3m2!1skk!2skz!4v1613777172782!5m2!1skk!2skz" width="100%" height="250" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        </div>
      </div>
      <q-separator dark class="q-mt-md" />
      <small class="q-pt-md text-grey-4">{{ year }} CipWiuim. Все права защищены.</small>
    </footer>

  </section>

</template>

<script>
export default {
  name: "cipFooter",
  computed: {
    contacts() {
      return this.$store.getters.getMainData.contacts
    },
    socials() {
      return this.$store.getters.getMainData.socials
    },
    year() {
      let date = new Date()
      return date.getFullYear()
    }
  }
}
</script>

<style lang="sass">
.footer
  margin-top: 150px
  text-align: center
  display: flex
  justify-content: center
  flex-direction: column
  margin-bottom: 30px

.footer-grid
  display: grid
  grid-template-columns: 1fr 1fr 1fr
  grid-gap: 30px
  align-items: center
  padding: 0 30px
  @media screen and (max-width: 650px)
    grid-template-columns: 1fr
    padding: 0 20px

  iframe
    border-radius: 4px
    box-shadow: 10px 10px 30px 0 rgba(0,0,0,.05)


  ul
    list-style-type: none

    li
      margin-left: 0 !important


.footer a
  line-height: 30px

</style>
