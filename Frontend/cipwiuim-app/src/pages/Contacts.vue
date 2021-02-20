<template>
  <q-page>
    <cip-bread-cumps current-page-title="Контакты"/>
    <cip-page-title title="Контакты" subtitle="Вы можете связаться с нами любым удобным для Вас способом"/>
    <section>
      <div class="contacts-grid q-mt-xl">
        <div>
          <div class="bg-white rounded-borders q-pa-md ">
            <q-icon name="room" size="30px" color="primary" class="q-mr-md"/>
            {{ contacts.address }}
          </div>
          <a :href="`tel:${contacts.phone}`" class="bg-white rounded-borders q-pa-md q-mt-md block">
            <q-icon name="call" size="30px" color="primary" class="q-mr-md"/>
            {{ contacts.phone }}
          </a>
          <a :href="`https://wa.me/${contacts.whatsapp}`" class="bg-white rounded-borders q-pa-md q-mt-md block">
            <q-icon name="mdi-whatsapp" size="30px" color="primary" class="q-mr-md"/>
            {{ contacts.whatsapp }}
          </a>
          <a :href="`mailto:${contacts.email}`" class="bg-white rounded-borders q-pa-md q-mt-md block">
            <q-icon name="alternate_email" size="30px" color="primary" class="q-mr-md"/>
            {{ contacts.email }}
          </a>

          <div class="bg-white rounded-borders q-pa-md q-mt-md">
            Мы в социальных сетях
            <div class="flex q-mt-sm">
              <div
                v-for="i in socials"
                :key="i.id"
              >
                <q-btn
                  :icon="i.icon"
                  color="primary"
                  round unelevated flat dense
                  class="q-mr-md"
                  type="a"
                  :href="i.url"
                  target="_blank"
                />
              </div>
            </div>
          </div>
          <cip-share class="q-mt-md"/>
        </div>
        <div>
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2903.508725349658!2d76.95652931571827!3d43.30360888298341!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x38836db517f8d783%3A0x951c31c0e3416169!2sCIP%20WIUIM!5e0!3m2!1skk!2skz!4v1613777172782!5m2!1skk!2skz" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
          </div>
      </div>
    </section>
  </q-page>
</template>

<script>
import CipPageTitle from "components/cipPageTitle";
import CipBreadCumps from "components/service/cipBreadCumps";
import CipShare from "components/service/cipShare";

export default {
  name: "Contacts",
  components: {CipShare, CipBreadCumps, CipPageTitle},
  computed: {
    contacts() {
      return this.$store.getters.getMainData.contacts
    },
    socials() {
      return this.$store.getters.getMainData.socials
    }
  }
}
</script>

<style lang="sass">
.contacts-grid
  display: grid
  grid-template-columns: 1fr 1fr
  grid-gap: 20px

  iframe
    border-radius: 4px
    box-shadow: 10px 10px 30px 0 rgba(0,0,0,.05)

  @media(max-width: 650px)
    grid-template-columns: 1fr
    grid-gap: 50px
</style>
